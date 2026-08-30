# Import the necessary libraries
import streamlit as st
import pandas as pd
import datetime
from pycaret.regression import load_model, predict_model

# 1. Page Configuration
# This sets the title and icon of the browser tab
st.set_page_config(page_title="Vaccine Predictor Dashboard", page_icon="💉", layout="centered")

# 2. Header and Main Description
st.title("💉 Global Vaccine Administration Forecaster")
st.markdown("""
Welcome to the **Vaccine Predictor Dashboard**! 
This application leverages an advanced **Extra Trees Machine Learning model** to forecast the number of daily COVID-19 vaccinations administered in a specific country.

*Behind the scenes:* The model uses historical temporal data and geographical features to make its estimations.
""")

st.divider()

# 3. Sidebar for User Inputs
st.sidebar.header("⚙️ Input Parameters")
st.sidebar.markdown("Specify the location and date to generate a forecast:")

# Input field for the country name
selected_country = st.sidebar.text_input("Country Name", value="United States").title()

# Set the historical boundaries for our dataset
min_date = datetime.date(2020, 12, 1)
max_date = datetime.date(2022, 12, 31)

# Input field for the date with safety boundaries
selected_date = st.sidebar.date_input(
    "Select Date",
    value=datetime.date(2021, 6, 1),
    min_value=min_date,
    max_value=max_date,
    help="Please select a date within the historical vaccination campaign (Dec 2020 - Dec 2022)."
)


# 4. Prediction Logic
# This block runs only when the user clicks the "Generate Forecast" button
if st.sidebar.button("Generate Forecast 🚀"):
    # Show a loading spinner while processing
    with st.spinner('Loading model and computing prediction...'):
        try:
            # Load the pre-trained PyCaret model (no need to add .pkl extension here)
            model = load_model('vaccination_et_model')

            # Prepare the input dictionary exactly as the model expects (Feature Engineering)
            input_dict = {
                'country': [selected_country],
                'year': [selected_date.year],
                'month': [selected_date.month],
                'day': [selected_date.day],
                'day_of_week': [selected_date.weekday()]
            }

            # Convert the dictionary into a Pandas DataFrame
            input_df = pd.DataFrame(input_dict)

            # Generate the prediction using PyCaret's predict_model function
            predictions = predict_model(model, data=input_df)

            # Extract the predicted value
            # Note: PyCaret 3.x stores the output in a column called 'prediction_label'
            pred_value = int(predictions['prediction_label'].iloc[0])

            # 5. Display the Results
            st.success("✨ Prediction Generated Successfully!")
            st.metric(label=f"Predicted Daily Vaccinations for {selected_country}",
                      value=f"{pred_value:,} doses")

            st.info(
                "💡 **Data Insight:** Tree-based models like this one excel at capturing non-linear trends, such as the day of the week or specific months when vaccination rates typically surge.")

        except Exception as e:
            # Handle any errors (e.g., if the model file is missing) gracefully
            st.error(f"An error occurred: {e}")
            st.warning("Please ensure 'vaccination_et_model.pkl' is in the same directory as this script.")