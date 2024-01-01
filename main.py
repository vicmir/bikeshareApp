# Importing necessary libraries for web application
import geocoder
import time
import folium
import webbrowser
from pywebio.input import input, select
from pywebio.output import put_text, put_button, put_image, put_table, put_error, put_tabs
from pywebio.platform.flask import webio_view
from flask import Flask, send_from_directory
from data_retrieval import get_stations_data
from distance_calculation import calculate_distances
from data_processing import process_station_data
from pywebio.session import run_js
from pywebio.session import download
from pywebio.output import put_html
from pywebio import config

# Initializing Flask app
app = Flask(__name__)

# Function to get user location
def get_user_location():
    current_location = geocoder.ip('me').latlng
    return current_location if current_location else None

# Main function for the web application
@config(theme='dark')
def main():
    # Get user location
    current_location = get_user_location()

    # Handling case where user location could not be determined
    if not current_location:
        put_error("The current user location could not be determined.")
        return

    # Extracting latitude and longitude from user location
    current_latitude, current_longitude = current_location

    # Get bike stations data
    all_stations = get_stations_data()

    # Handling case where data retrieval fails
    if not all_stations:
        put_error("Error while receiving data.")
        return

    # Process data for all stations
    stations_list = []
    for station in all_stations:
        station_info = station['properties']
        station_data = process_station_data(station)
        stations_list.append(station_data)

    # Calculate distances for all stations
    calculate_distances(stations_list, current_location)

    # Displaying the application logo
    put_image('/static/logo.jpg', width='100%', height='50%')

    # Input parameters from the user
    search_param = select("Select a search parameter", options=["Bikes", "Docks"])

    # Entering the minimum number of free docks/bikes
    min_available_str = input("Enter the minimum number of free docks/bikes or 'all' for all")

    # Validate input for minimum available
    while not min_available_str.isdigit() and min_available_str.lower() != 'all':
        min_available_str = input("Invalid input. Please enter a number or 'all' for all")

    # Entering the number of results to display
    K_str = input("Enter the number of results to display or 'all' for all")

    # Validate input for results count
    while not K_str.isdigit() and K_str.lower() != 'all':
        K_str = input("Invalid input. Please enter a number or 'all' for all")

    # Convert input to integers
    min_available = int(min_available_str) if min_available_str.isdigit() else 0
    K = int(K_str) if K_str.isdigit() else len(stations_list)

    # Defining sorting criteria based on user input
    if search_param == "Bikes":
        sort_criterion = "bikes_available"
    else:
        sort_criterion = "docks_available"

    # Sort stations based on sorting criteria
    sorted_stations = sorted(stations_list, key=lambda x: (x[sort_criterion] >= min_available, x['distance']))

    # Filtering nearby stations based on user input
    nearest_stations = [station for station in sorted_stations if station[sort_criterion] >= min_available][:K]

    # Displaying nearby stations in a table
    line = " "
    put_text(line) # ...

    # Displaying an error message if no results are found
    if len(nearest_stations) == 0:
        put_error("No results found.")
    # Displaying table headers
    else:
        table_data = [["Station", "Bikes", "Docks", "Distance (km)"]]

        # Populating table with data for nearby stations
        for station in nearest_stations[:K]:
            table_data.append([station['name'], str(station['bikes_available']), str(station['docks_available']), str(station['distance'])])
        # Displaying the table
        put_table(table_data)

    # Displaying a button to allow user to reenter data
    put_button("Reenter data", onclick=lambda: run_js("location.reload()"))

    # Creating a map using Folium
    m = folium.Map(location=[current_latitude, current_longitude], zoom_start=14)

    # Adding markers for user location and nearby stations
    folium.Marker([current_latitude, current_longitude], popup='Your location').add_to(m)

    # Adding markers and route lines for nearby stations
    for station in nearest_stations[:K]:
        folium.Marker([station['latitude'], station['longitude']],
                      popup=f"Station: {station['name']}, Bikes: {station['bikes_available']}, Docks: {station['docks_available']}, Distance: {station['distance']} km").add_to(m)

        # Adding a route line
        folium.PolyLine(locations=[(current_latitude, current_longitude), (station['latitude'], station['longitude'])],
                        weight=5, color='blue').add_to(m)

    # Save the map to the static folder
    m.save('static/route_map.html')

    # Generating a timestamp to ensure map refreshes
    timestamp = int(time.time())
    put_text(line)

    # Displaying the map using an iframe
    put_html(f'<iframe src="/static/route_map.html?{timestamp}" width="100%" height="500px"></iframe>')
    map_file_path = 'static/route_map.html'

    # Displaying a button to allow user to download the map
    put_button("Save map", onclick=lambda: download('route_map.html', open(map_file_path, 'rb').read()))

# Serve the map file using Flask's send_from_directory
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

# Run the web application
if __name__ == "__main__":
    # Use Flask to create a web view
    webbrowser.open('http://localhost:80/app')
    app.add_url_rule('/app', 'webio_view', webio_view(main), methods=['GET', 'POST', 'OPTIONS'])
    app.run(host='localhost', port=80, debug=True)