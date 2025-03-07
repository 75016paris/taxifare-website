import streamlit as st
import pandas as pd
import requests
from datetime import datetime

'''
# LOOSER TAXI APP WELCOM
'''

st.markdown(f'''
We are a space travel company

Please provide your location and desination,

The space shuttle will pick you up in asap
''')

pickup_datetime = st.text_input("Date & Time", value=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428)

pickup_latitude = st.number_input("Pickup Latitude", value=40.748817)

dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985428)

dropoff_latitude = st.number_input("Dropoff Latitude", value=40.748817)

passenger_count = st.number_input("Number of Passengers", min_value=1, max_value=6, value=1)


# X_new = pd.DataFrame(dict(date_and_time=[date_and_time],
#                           pickup_longitude=[pickup_longitude],
#                           pickup_latitude=[pickup_latitude],
#                           dropoff_longitude=[dropoff_longitude],
#                           dropoff_latitude=[dropoff_latitude],
#                           passenger_count=[passenger_count]))

# st.write(X_new)

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
