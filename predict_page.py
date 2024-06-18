import streamlit as st

# Function to show the prediction page
def show_predict_page():
    st.title("Software Developer Salary Prediction")
    st.write("We need some information to predict the salary")

    # Sample countries list
    countries = ["United States", "Canada", "India", "United Kingdom", "Germany"]

    # Ensure unique keys for each widget
    country = st.selectbox("Country", countries, key="country_selectbox_predict_unique")

    # Add other widgets with unique keys
    experience = st.slider("Years of Experience", 0, 20, key="experience_slider_predict_unique")

    # Process prediction based on input
    if st.button("Predict", key="predict_button_unique"):
        st.write(f"Prediction for {country} with {experience} years of experience.")

# Example cache usage (adjust based on what you need to cache)
@st.cache_data
def load_data():
    # Load your data here
    pass
