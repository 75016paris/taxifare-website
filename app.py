import streamlit as st
import pandas as pd
import requests

'''
# LOOSER TAXI APP WELCOM
'''

st.markdown(f'''
We are a space travel company

Please provide your location and desination,

The space shuttle will pick you up in asap
''')

pickup_datetime = st.text_input('pickup datetime', '2014-07-06 19:18:00')

pickup_longitude = st.text_input('pickup longitude')

pickup_latitude = st.text_input('pickup latitude')

dropoff_longitude = st.text_input('dropoff longitude')

dropoff_latitude = st.text_input('dropoff latitude')

passenger_count = st.number_input('passenger count', min_value=1, max_value=8, step=1)


# X_new = pd.DataFrame(dict(date_and_time=[date_and_time],
#                           pickup_longitude=[pickup_longitude],
#                           pickup_latitude=[pickup_latitude],
#                           dropoff_longitude=[dropoff_longitude],
#                           dropoff_latitude=[dropoff_latitude],
#                           passenger_count=[passenger_count]))

# st.write(X_new)

url = 'https://taxifare.lewagon.ai/predict'

params = {
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_longitude,
    'pickup_latitude': pickup_latitude,
    'dropoff_longitude': dropoff_longitude,
    'dropoff_latitude': dropoff_latitude,
    'passenger_count': passenger_count
}

response = requests.get(url, params=params)
prediction = response.json()

st.write(f"Prediction: {prediction}")
'''
