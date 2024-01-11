# Importing necessary libraries for distance calculation
from math import radians, sin, cos, sqrt, atan2

# Function to calculate the haversine distance between two sets of latitude and longitude coordinates
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 # Radius of the Earth in kilometers
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    # Calculating differences in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Haversine formula for distance calculation
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance

# Function to calculate distances for all stations based on the user's current location
def calculate_distances(stations_list, current_location):
    for station_data in stations_list:
        # Calculating distance using the haversine formula
        distance = haversine(current_location[0], current_location[1], station_data["latitude"], station_data["longitude"])
        station_data["distance"] = distance