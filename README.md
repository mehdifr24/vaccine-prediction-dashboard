# 💉 Vaccine Administration Forecasting & Dashboard

## 📖 About

This project demonstrates an end-to-end supervised machine learning workflow and software deployment for predicting the number of daily COVID-19 vaccinations administered across different countries. 
The pipeline includes data cleaning, exploratory data analysis (EDA), temporal feature engineering, automated model selection using PyCaret, and deploying the final predictive model as an interactive web application using Streamlit.

## 🚀 Technologies

* Python
* Pandas & NumPy
* Matplotlib & Seaborn
* PyCaret (AutoML)
* Streamlit (Web Deployment)

## 📂 Dataset

The dataset involves global COVID-19 vaccination records, capturing metrics like total vaccinations, daily vaccinations, and manufacturer details across various countries. By extracting temporal features (year, month, day, day of the week) from the dates, the problem is structured as a Supervised Regression task to forecast daily doses.

## 📊 Project Workflow

* Data Cleaning & Handling Missing Values (Forward-fill strategy)
* Exploratory Data Analysis (EDA) & Storytelling
* Feature Engineering (Extracting datetime components)
* Automated Model Training & Comparison (PyCaret)
* Identifying Feature Importance
* Finalizing & Saving the Best Pipeline (.pkl)
* Building an Interactive UI & Web Deployment (Streamlit)

## 📈 Model Performance

To evaluate the regression algorithms, standard metrics such as R-Squared (higher is better) and RMSE (lower is better) were utilized during the PyCaret comparison phase. Tree-based models heavily outperformed linear models in capturing non-linear temporal waves.

| Model | R-Squared (R²) | RMSE | MAE |
| :--- | :---: | :---: | :---: |
| **Extra Trees Regressor** | 0.9968 | 42,835 | 6,545 |
| **Random Forest Regressor** | 0.9934 | 62,831 | 8,493 |
| **Decision Tree Regressor** | 0.9909 | 72,196 | 8,679 |

## 📊 Results Visualization

**1. Global Vaccination Temporal Waves (EDA)**

<img width="1384" height="584" alt="image" src="https://github.com/user-attachments/assets/594c6eb1-d9a8-42f4-bafa-86adcaaa1f32" />


**2. Model Feature Importance**

<img width="751" height="468" alt="image" src="https://github.com/user-attachments/assets/1961debb-04e2-48fa-b112-90822167ff31" />


**3. Interactive Streamlit Dashboard**

<img width="2229" height="1247" alt="image" src="https://github.com/user-attachments/assets/466f0461-d11e-466f-a440-551f5d0d9ba6" />




## 🏆 Final Model Selection & Deployment Strategy

The **Extra Trees Regressor** was selected as the final model due to its near-perfect R² score and its robust ability to handle categorical geographic data (countries) alongside non-linear temporal features (months, days). 

**Business & Technical Insights:**
1. **Temporal Dominance:** The model heavily relied on temporal features, proving that vaccination rollouts occurred in distinct chronological "waves".
2. **Extrapolation Handling:** Tree-based models cannot extrapolate beyond their training timeline. To ensure a robust user experience, the Streamlit UI was engineered with strict date boundaries matching the historical data.

The finalized model was deployed into a production-ready **Streamlit** dashboard, allowing users to select a specific country and date to generate real-time forecasts.

## 💻 How to Run Locally

To explore the model and interact with the dashboard on your own machine, simply open your terminal and run the following commands sequentially:

```bash
# 1. Clone the repository and navigate into it
git clone [https://github.com/mehdifr24/vaccine-prediction-dashboard.git](https://github.com/mehdifr24/vaccine-prediction-dashboard.git)
cd vaccine-prediction-dashboard

# 2. Create and activate a virtual environment (Windows)
# (For macOS/Linux, use: source venv/bin/activate)
python -m venv venv
venv\Scripts\activate

# 3. Install the required dependencies
pip install -r requirements.txt

# 4. Launch the Streamlit dashboard
python -m streamlit run app.py

```

## 👨‍💻 Author

**Mehdi Ferdosi**

Computer Science Student | Machine Learning Enthusiast

GitHub: https://github.com/mehdifr24
