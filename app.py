import streamlit as st
import pandas as pd
import numpy as np

'''
# LOOSER TAXI APP WELCOM
'''

st.markdown(f'''
We are a space travel company

Please provide your location and desination
The space shuttle will pick you up in {np.random(100,3300)}
''')


date_and_time = st.text_input('date and time')

pickup_longitude = st.text_input('pickup longitude')

pickup_latitude = st.text_input('pickup latitude')

dropoff_longitude = st.text_input('dropoff longitude')

dropoff_latitude = st.text_input('dropoff latitude')

passenger_count = st.number_input('passenger count', min_value=1, max_value=8, step=1)


X_new = pd.DataFrame(dict(date_and_time=[date_and_time],
                          pickup_longitude=[pickup_longitude],
                          pickup_latitude=[pickup_latitude],
                          dropoff_longitude=[dropoff_longitude],
                          dropoff_latitude=[dropoff_latitude],
                          passenger_count=[passenger_count]))

st.write(X_new)


'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''


date and time = st.text_input('date and time', '01/01/00')
pickup longitude = st.text_input('pickup longitude')
pickup latitude = st.text_input('pickup latitude')
dropoff longitude = st.text_input('dropoff longitude')
dropoff latitude = st.text_input('dropoff latitude')
passenger count = st.text_input('passenger count')



########################################################################################################################

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
