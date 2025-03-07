import streamlit as st
import pandas as pd
import requests
import numpy as np
from datetime import datetime
import folium
from streamlit_folium import st_folium
from folium.plugins import Geocoder

'''
# SPACE TRAVEL TAXI CO.
'''

st.markdown(f'''
We are a space travel company,

Please provide your location and destination.

We will warp a vessel toward your destination as soon as possible.

\n
### WARNING
_Make sure to hold on to your wig, the wormholes opening, could suck it in_
''')

pickup_date = st.date_input("Pickup Date", value=datetime.now().date())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())
pickup_datetime = datetime.combine(pickup_date, pickup_time).strftime("%Y-%m-%d %H:%M:%S")

# Default coordinates
pickup_longitude = -73.985428
pickup_latitude = 40.748817
dropoff_longitude = -73.985428
dropoff_latitude = 40.748817


# Create a map centered around the default pickup location
map = folium.Map(location=[pickup_latitude, pickup_longitude], zoom_start=15)

# Add draggable markers for pickup and dropoff locations
pickup_marker = folium.Marker(
    [pickup_latitude, pickup_longitude],
    popup="Pickup Location",
    icon=folium.Icon(color="green"),
    draggable=True
)
dropoff_marker = folium.Marker(
    [dropoff_latitude+0.005, dropoff_longitude+0.005],
    popup="Dropoff Location",
    icon=folium.Icon(color="red"),
    draggable=True
)

pickup_marker.add_to(map)
dropoff_marker.add_to(map)


url2  = 'https://nominatim.openstreetmap.org/search?'

pickup_adress = st.text_input('pickup_adress', value=pickup_adress, key='pickup_adress')
dropoff_adress = st.text_input('dropoff_adress', value=dropoff_adress, key='dropoff_adress')

if st.button("Adress"):
    params2 = {
        "pickup_adress": dropoff_adress,
        "dropoff_adress": dropoff_adress
    }
    response = requests.get(url2, params=params2)

    prediction = response.json().get("fare", "Error")
    st.markdown(prediction)

# Display the map
map_data = st_folium(map, width=700, height=500)

# Display updated coordinates in input fields
pickup_longitude_input = st.number_input("Pickup Longitude", value=pickup_longitude, key="pickup_longitude")
pickup_latitude_input = st.number_input("Pickup Latitude", value=pickup_latitude, key="pickup_latitude")
dropoff_longitude_input = st.number_input("Dropoff Longitude", value=dropoff_longitude, key="dropoff_longitude")
dropoff_latitude_input = st.number_input("Dropoff Latitude", value=dropoff_latitude, key="dropoff_latitude")
passenger_count = st.number_input("Number of Passengers", min_value=1, max_value=6, value=1)

url = 'https://taxifare.lewagon.ai/predict'

if st.button("Predict Fare"):
    params = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": pickup_longitude,
        "pickup_latitude": pickup_latitude,
        "dropoff_longitude": dropoff_longitude,
        "dropoff_latitude": dropoff_latitude,
        "passenger_count": passenger_count,
    }

    response = requests.get(url, params=params)

    prediction = response.json().get("fare", "Error")
    st.markdown(f"##  Fare: ${prediction:.2f}")
