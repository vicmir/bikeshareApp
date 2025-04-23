# 🚲 Bike Station Live Feed 

The project aims to leverage data science techniques to analyze the live feed of bike stations, specifically focusing on finding the nearest bike stations based on available bikes or docks and presenting a route on Google Maps for bike users. Developed application helps users find nearby bike share stations and plan their routes. The application retrieves real-time bike station data, processes it, and presents the information to the user in a visually appealing manner. To achieve these goals, the live feed of Metro Bike Share in Los Angeles city was processed. More specifically, the data collected in a file in JSON format was used.

Given the dataset containing bike station information and the requirement to parse the live feed to find the nearest bike stations, the project addresses three main tasks:
1. Finding K-nearest bike stations based on available bikes for a person without a bike.
2. Finding K-nearest bike stations where docks are available for a person with a bike.
3. Presenting a route on Google Maps from a source to a destination using only foot and bike transport.

## 📌 Features

- **User Location:** Automatically detects the user's location using their IP address.
- **Search Parameters:** Allows users to choose between searching for available bikes or docks.
- **Filtering Options:** Users can set filters for the minimum number of available docks or bikes and the number of results to display.
- **Interactive Map:** Displays a map with the user's location, nearby stations, and the route to the selected station.
- **Results Table:** Presents a table with detailed information about nearby stations, including the station name, bikes available, docks available, and distance from the user.

## 📌 Module, data structures, tools used in the project

 📍 **Tools:**
- **Python:** The primary programming language for data processing and analysis.
- **Jupyter Notebook:** Utilized for interactive development, testing, and documentation of code snippets.
- **PyCharm:** Employed as an integrated development environment (IDE) for more efficient coding, debugging, and project management.

 📍 **Algorithms:**
- **Haversine Formula:** Applied to calculate geographical distances between user locations and bike stations.

 📍 **Modules:**
- **requests:** Utilized for making HTTP requests to fetch real-time bike station data.
- **JSON:** Used for parsing and extracting information from the JSON data received from the bike station live feed.
- **geocoder:** For visualizing geographical data in assisting in obtaining user location.
- **folium:** For visualizing geographical data in creating interactive maps.
- **Flask:** Employed as a web framework to develop the main web application. Flask facilitates the handling of HTTP requests, routing, and overall web application structure.
- **PyWebIO:** Integrated for creating an interactive web interface to facilitate user input and display the results in the web application.

 📍 **Data Structures:**
- **Dictionaries:** Utilized to store and organize station information with key-value pairs, providing a structured format for processing and presenting data.
- **Lists:** Employed to store and manipulate ordered station data, enabling efficient iteration and sorting.

 📍 **APIs:**
- **Google Maps API:** Utilized to obtain routing information and visualize bike routes on Google Maps, enhancing the user experience.
- **Bike Station Live Feed API:** Employed to fetch real-time data on bike station information, ensuring the application reflects the most recent status of bike stations.

## 📌 Prerequisites

Before running the application, make sure that you are connected to the internet and that you have the following dependencies installed:

- Python 3.x
- Flask
- PyWebIO
- Requests
- Folium

Install the dependencies using the following command:

```
pip install flask pywebio requests folium
```

## 📌 How to Run this application

### 📍 Step 1. Run the application localy or clone the repository:
```
git clone https://github.com/vicmir/bikeshareApp.git

cd bikeshareApp
```

### 📍 Step 2. Run the application:
```
python main.py
```

### 📍 Step 3. After running the application, the browser will be opened automatically at http://localhost:80/app

### 📍 Step 4. Chose a search parameter (bikes or docks):

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/af52bddc-ca21-4436-9655-d4fa370b2b29)

### 📍 Step 5. Chose minimum number of free bikes or docks required or enter "all":

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/aa8856fe-bbcf-48eb-8bf6-6e1a22ba7a3d)

### 📍 Step 6. Chose number of search results to be displayed:

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/14fb26ca-d18d-4f15-9d63-15fdadaa4bbd)

### 📍 Step 7. Reenter data or save the map with routes:

![image](https://github.com/vicmir/bikeshareApp/assets/79836020/61c764a4-aae0-4198-b57d-48bdc20da325)
![image](https://github.com/vicmir/bikeshareApp/assets/79836020/d09550b9-9b69-4911-951d-7b37606bd4ff)
