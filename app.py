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


if 'pickup_set' not in st.session_state:
    st.session_state.pickup_set = False

if 'dropoff_set' not in st.session_state:
    st.session_state.dropoff_set = False

def get_map_data():
    data = []
    if st.session_state.pickup_set:
        data.append([st.session_state.pickup_longitude, st.session_state.pickup_latitude])
    if st.session_state.dropoff_set:
        data.append([st.session_state.dropoff_longitude, st.session_state.dropoff_latitude])
    return pd.DataFrame(data, columns=['lon', 'lat'])

df = get_map_data()

st.map(df)

if not st.session_state.pickup_set:
    if st.button("Set Pickup Location"):
        st.session_state.pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)
        st.session_state.pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)
        st.session_state.pickup_set = True
else:
    st.write(f"Pickup Location set at: ({st.session_state.pickup_longitude}, {st.session_state.pickup_latitude})")

if st.session_state.pickup_set and not st.session_state.dropoff_set:
    if st.button("Set Dropoff Location"):
        st.session_state.dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)
        st.session_state.dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)
        st.session_state.dropoff_set = True
else:
    if st.session_state.dropoff_set:
        st.write(f"Dropoff Location set at: ({st.session_state.dropoff_longitude}, {st.session_state.dropoff_latitude})")

pickup_date = st.date_input("Pickup Date", value=datetime.now().date())
pickup_time = st.time_input("Pickup Time", value=datetime.now().time())
pickup_datetime = datetime.combine(pickup_date, pickup_time).strftime("%Y-%m-%d %H:%M:%S")

pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)

pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)

dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)

dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

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
