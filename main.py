import streamlit as st
import pandas as pd

# -----------------


# --------------------  [] --------------------
st.title('Weather Analysis')
data_latitude = st.sidebar.slider('Latitude', min_value=-90.0, max_value=90.0, value=37.76, step=0.01)
data_longitude = st.sidebar.slider('Longitude', min_value=-180.0, max_value=180.0, value=-122.4, step=0.01)
location = st.text_input("Enter the location")
st.write('The current location is:', location)

# all variables
data_temp_f = None
data_temp_c = None 
feel_c = None 
feel_f = None
uv_index = None 
gust_kph  = None
# air quality
data_quality = None

search_button = st.button('Search')
if(search_button):
    get_data = pd.read_json("http://api.weatherapi.com/v1/current.json?key=b74e9e08b8dd4d498ca64513242003&q={}&aqi=yes".format(location))
    data_latitude = get_data.loc['lat']['location']
    data_longitude = get_data.loc['lon']['location']

    data_temp_f = get_data.loc['temp_f']['current']
    data_temp_c = get_data.loc['temp_c']['current']
    feel_c = get_data.loc['feelslike_c']['current']
    feel_f = get_data.loc['feelslike_f']['current']
    uv_index = get_data.loc['uv']['current']
    gust_kph = get_data.loc['gust_kph']['current']
    # air quality
    data_quality = get_data.loc['air_quality']['current']
# Create dataframe
df = pd.DataFrame(
    [[data_latitude, data_longitude]],
    columns=['lat', 'lon'])

st.map(df)  # main data

# all data points are here
st.subheader('Temperature')
st.write('Temperature in Celsius:', data_temp_c)
st.write('Temperature in Fahrenheit:', data_temp_f)
st.write('Feels like in Celsius:', feel_c)
st.write('Feels like in Fahrenheit:', feel_f)
st.write('UV Index:', uv_index)
st.write('Gust in Kph:', gust_kph)
# air quality
st.bar_chart(data_quality,)




