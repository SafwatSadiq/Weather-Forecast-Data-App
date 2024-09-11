import streamlit as st

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=0, max_value=5,
                       help="Select the number of days to forecast")
options = st.selectbox("Select data to view",
                       options=('Temperature', 'Sky'))
st. subheader(f"{options} for the next {days} days in {place.title()}")