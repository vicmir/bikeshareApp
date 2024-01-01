# Importing the requests module for making HTTP requests
import requests

# Function to retrieve bike stations data from the specified URL
def get_stations_data():
    # URL for fetching bike station data
    url = "http://bikeshare.metro.net/stations/json/"
    # Headers to simulate a user agent (didn't work other way)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    # Making a GET request to the specified URL
    response = requests.get(url, headers=headers)
    # Checking if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json() # Parsing the JSON response and returning the 'features' data
        return data['features']
    else:
        return None # Returning None in case of an error