import streamlit as st
import requests

st.title("TaxiFareModel front")

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

# Existing content
st.title("TaxiFareModel front")

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

# New content for prediction
st.markdown('''
## Taxi Fare Prediction

Enter the details below to get a prediction for your taxi ride fare:
''')

# Input fields for parameters
pickup_latitude = st.number_input("Pickup Latitude", value=40.747)
pickup_longitude = st.number_input("Pickup Longitude", value=-73.989)
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.802)
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.956)
passenger_count = st.number_input("Number of Passengers", min_value=1, value=2)
pickup_datetime = st.text_input("Pickup Date/Time", value="2024-12-06 15:44:10")

# Submit button to trigger API call
if st.button('Get Prediction'):
    # Construct the data dictionary
    data = {
        "pickup_latitude": pickup_latitude,
        "pickup_longitude": pickup_longitude,
        "dropoff_latitude": dropoff_latitude,
        "dropoff_longitude": dropoff_longitude,
        "passenger_count": passenger_count,
        "pickup_datetime": pickup_datetime
    }

    # Send a GET request to the API with the parameters
    url = 'https://taxifare.lewagon.ai/predict'
    response = requests.get(url, params=data)

    # If the response is successful, display the predicted fare
    if response.status_code == 200:
        fare = response.json()['fare']
        st.write(f"The predicted fare is ${fare:.2f}")
    else:
        st.error("Failed to fetch prediction. Please try again.")
