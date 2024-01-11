# Project 4: Bike Station Live Feed. 

This is a web application that helps users find nearby bike share stations and plan their routes. The application retrieves real-time bike station data, processes it, and presents the information to the user in an interactive and visually appealing manner.

## Features

- **User Location:** Automatically detects the user's location using their IP address.
- **Search Parameters:** Allows users to choose between searching for available bikes or docks.
- **Filtering Options:** Users can set filters for the minimum number of available docks or bikes and the number of results to display.
- **Interactive Map:** Displays a map with the user's location, nearby stations, and the route to the selected station.
- **Results Table:** Presents a table with detailed information about nearby stations, including the station name, bikes available, docks available, and distance from the user.

## Prerequisites

Before running the application, the following dependencies should be installed:

- Python 3.x
- Flask
- PyWebIO
- Requests
- Folium

Install the dependencies using the following command:

```
pip install flask pywebio requests folium
```

## How to Run this application

### Step 1. Clone the repository:
```
git clone https://github.com/vicmir/bikeshareApp.git

cd bikeshareApp
```

### Step 2. Run the application:
```
python main.py
```

### Step 3. After running the application, the browser will be opened automatically at http://localhost:80/app

### Step 4. Chose a search parameter (bikes or docks):

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/af52bddc-ca21-4436-9655-d4fa370b2b29)

### Step 5. Chose minimum number of free bikes or docks required or enter "all":

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/aa8856fe-bbcf-48eb-8bf6-6e1a22ba7a3d)

### Step 6. Chose number of search results to be displayed:

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/14fb26ca-d18d-4f15-9d63-15fdadaa4bbd)

### Step 7. Reenter data or save the map with routes:

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/61c764a4-aae0-4198-b57d-48bdc20da325)

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/d09550b9-9b69-4911-951d-7b37606bd4ff)

