import streamlit as st

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

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

st.write('The current movie title is', title)

date and time
pickup longitude
pickup latitude
dropoff longitude
dropoff latitude
passenger count

def get_slider_data():

    return pd.DataFrame({
          'first column': list(range(1, 11)),
          'second column': np.arange(10, 101, 10)
        })

df = get_slider_data()

option = st.slider('Select a modulus', 1, 10, 3)

filtered_df = df[df['first column'] % option == 0]

st.write(filtered_df)


2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
