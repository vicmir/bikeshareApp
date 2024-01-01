# Function to process individual station data obtained from the JSON response
def process_station_data(station):
    # Extracting relevant information from the station properties
    station_info = station['properties']
    # Creating a dictionary to store processed station information
    return {
        'name': station_info['name'],
        'address': station_info['addressStreet'],
        'bikes_available': station_info['bikesAvailable'],
        'docks_available': station_info['docksAvailable'],
        'latitude': station_info['latitude'],
        'longitude': station_info['longitude']
    }