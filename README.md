# RISING WATER

## Project Overview

Floods are one of the most devastating natural disasters. This project uses Machine Learning algorithms to predict the likelihood of flood occurrence based on weather and rainfall parameters.

## Features

- Flood Risk Prediction
- Machine Learning Based Analysis
- Random Forest Classification Model
- Flask Web Application
- User-Friendly Interface

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Flask
- HTML
- CSS

## Dataset Features

- Temperature
- Humidity
- Cloud Cover
- Annual Rainfall
- Jan-Feb Rainfall
- Mar-May Rainfall
- Jun-Sep Rainfall
- Oct-Dec Rainfall
- Average June Rainfall
- Sub Rainfall

## Machine Learning Models Used

1. Decision Tree
2. Random Forest
3. K-Nearest Neighbors (KNN)

## Model Performance

| Model | Accuracy |
|---------|---------|
| Decision Tree | 100% |
| Random Forest | 100% |
| KNN | 91.30% |

## Project Structure

```text
FloodPredictionProject
│
├── app.py
├── train.py
├── flood.csv
├── model.pkl
├── scaler.pkl
│
├── templates
│   └── index.html
│
├── static
│   └── style.css
│
└── README.md
```

## How to Run

1. Install required libraries

```bash
pip install pandas numpy scikit-learn flask joblib
```

2. Run Flask application

```bash
python app.py
```

3. Open browser

```text
http://127.0.0.1:5000
```

## Future Scope

- Real-time weather API integration
- Cloud deployment using IBM Cloud
- Mobile application support
- Advanced flood forecasting models

## Team Members

- Sunkara Devi Prasanna (Team Lead)  
- Parasa Haritha
- Kakarla Lakshmi Venkata Siva Sai Konda
- Jasmin Shaik 
- Sharukh Mohmammad

## Project Outcome

The system successfully predicts flood occurrence using machine learning techniques and provides a simple web interface for users to check flood risk.
