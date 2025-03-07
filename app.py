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


date_and_time = st.text_input('date and time', '01/01/00')

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



'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

params = {
    'date_and_time': date_and_time,
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

https://taxifare-154686505166.europe-west1.run.app

########################################################################################################################

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
