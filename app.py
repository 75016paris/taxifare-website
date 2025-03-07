import streamlit as st
import pandas as pd
import requests
import numpy as np
from datetime import datetime
import folium
from streamlit_folium import st_folium

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

def geocode_address(address):
    base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
    params = {'address': 'address'}
    response = requests.get(base_url, params=params)
    results = response.json()['results']
    if results:
        location = results:inlineRefs{references="&#91;&#123;&quot;type&quot;&#58;&quot;inline_reference&quot;,&quot;start_index&quot;&#58;1103,&quot;end_index&quot;&#58;1106,&quot;number&quot;&#58;0,&quot;url&quot;&#58;&quot;https&#58;//discuss.streamlit.io/t/streamlit-geolocation/30796&quot;,&quot;favicon&quot;&#58;&quot;https&#58;//imgs.search.brave.com/cnP-AtwWHvcfbMyCt2bZ8l9b_AiXSYteLVK99iJ4Deo/rs&#58;fit&#58;32&#58;32&#58;1&#58;0/g&#58;ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvYTBmZjE3NGY2/NjhlOGVhN2RjNGQ2/ODdmMDJjMmJiZGM0/OWE5YjU4ZWVkMmEx/YzMzZmE4YjkyYzI5/NDRlZjg3My9kaXNj/dXNzLnN0cmVhbWxp/dC5pby8&quot;,&quot;snippet&quot;&#58;&quot;Get&#32;User&#32;Location&#32;Button&#32;Show&#32;the&#32;Community!&#32;components&#58;&#32;Web&#32;Geolocation&#32;API&#32;to&#32;Get&#32;User's&#32;Location&#32;Using&#32;Streamlit&#32;geospatial&#32;•&#32;May&#32;14,&#32;2024&#58;&#32;April&#32;2,&#32;2024…&quot;&#125;&#93;"}['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None

location['lat'], location['lng'] = geocode_address('32 Mott Street')
location['lat'], location['lng']

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
