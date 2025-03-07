import streamlit as st
import pandas as pd
import requests
import numpy as np
from datetime import datetime


'''
# SPACE TRAVEL TAXI CO.
'''

st.markdown(f'''
We are a space travel company,

Please provide your location and desination.

We will warp a vessel toward your destination as soon as possible.

\n
### WARNING
_Make sure to hold on to your wig, the wormholes opening, could suck it in_
''')


pickup_date = st.date_input("Pickup Date", value=datetime.now().date())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())
pickup_datetime = datetime.combine(pickup_date, pickup_time).strftime("%Y-%m-%d %H:%M:%S")

pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)

pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)

dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)

dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

passenger_count = st.number_input("Number of Passengers", min_value=1, max_value=6, value=1)


# def get_map_data():
#     return pd.DataFrame(
#         [[pickup_longitude, pickup_latitude], [dropoff_longitude, dropoff_latitude]],
#         columns=['lon', 'lat']
#     )

# df = get_map_data()

# st.map(df)

pickup = pd.DataFrame({
    'latitude': [pickup_latitude],
    'longitude': [pickup_longitude]
})

dropoff = pd.DataFrame({
    'latitude': [pickup_latitude],
    'longitude': [pickup_longitude]
})

st.map(pickup, dropoff, zoom=15)


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

# params = {
#     'pickup_datetime': pickup_datetime,
#     'pickup_longitude': pickup_longitude,
#     'pickup_latitude': pickup_latitude,
#     'dropoff_longitude': dropoff_longitude,
#     'dropoff_latitude': dropoff_latitude,
#     'passenger_count': passenger_count
# }

# response = requests.get(url, params=params)
# prediction = response.json()

# st.write(f"Prediction: {prediction}")
# '''
