# Bike Share Project

This is a web application that helps users find nearby bike share stations and plan their routes. The application retrieves real-time bike station data, processes it, and presents the information to the user in an interactive and visually appealing manner.

## Features

- **User Location:** Automatically detects the user's location using their IP address.
- **Search Parameters:** Allows users to choose between searching for available bikes or docks.
- **Filtering Options:** Users can set filters for the minimum number of available docks or bikes and the number of results to display.
- **Interactive Map:** Displays a map with the user's location, nearby stations, and the route to the selected station.
- **Results Table:** Presents a table with detailed information about nearby stations, including the station name, bikes available, docks available, and distance from the user.

## Prerequisites

Before running the application, make sure you have the following dependencies installed:

- Python 3.x
- Flask
- PyWebIO
- Requests
- Folium

Install the dependencies using the following command:

```bash
pip install flask pywebio requests folium

## How to Run

1. Clone the repository:
git clone https://github.com/your-username/bike-share-project.git
cd bike-share-project

2. Run the application:
python main.py

3. Open your browser and go to http://localhost:80/app to access the application.

## Screenshots