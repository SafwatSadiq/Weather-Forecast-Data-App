import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                       help="Select the number of days to forecast")
option = st.selectbox("Select data to view",
                       options=('Temperature', 'Sky'))
if place:
    try:
        # Get the temperature/sky data
        data, dates, conditions = get_data(place, days, option)
    except KeyError:
        st.error("Invalid city name or data not available.")
    else:
        # Add sub header
        st. subheader(f"{option} for the next {days} days in {place.title()}")

        if option == 'Temperature':
            figure = px.line(x=dates, y=data, labels={'x': "Date", 'y': "Temperature(C)"})
            st.plotly_chart(figure)

        if option == 'Sky':
            images = {"Clear": "images/clear.png", "Clouds" : "images/cloud.png",
                    "Rain": "images/rain.png", "Snow": "images/snow.png"}
            image_paths = [images[condition] for condition in data]
            # caption = [conditions[i] + ' | ' + dates[i] for i in range(len(dates))]
            caption = [f"Condition: {conditions[i]} \n Date: {dates[i]}" for i in range(len(dates))]
            st.image(image_paths, width=140, caption=caption)