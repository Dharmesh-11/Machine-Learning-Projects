# Big Mart Sales Prediction – Machine Learning Web Application

## Project Overview
This project predicts sales of a product in a retail store based on various features such as product weight, visibility, outlet type, store size, etc. 
The model is trained using XGBoost Regressor, and a Flask web application is used to deploy the model for real-time predictions.

## Features
- Data cleaning and preprocessing
- Label encoding for categorical values
- Model training using XGBoost
- Web interface built with Flask + Bootstrap
- User inputs product features and gets predicted sales instantly
- Model saved and reused using pickle

## Project Structure
```
BigMart-Sales-Prediction/
│── app.py                 # Flask app file
│── model.pkl              # Trained ML model
│── requirements.txt       # Dependencies
│── README.md              # Project Documentation
└── templates/
      └── index.html       # Frontend UI
```

## Technologies Used
| Technology | Purpose |
|----------|---------|
| Python | Programming Language |
| Pandas / NumPy | Data Analysis & Processing |
| Scikit-Learn | Preprocessing & Model Evaluation |
| XGBoost | Machine Learning Model |
| Flask | Web Framework |
| HTML / CSS / Bootstrap | Frontend UI |

## Installation & Setup

### 1. Clone the Repository
```
git clone https://github.com/Dharmesh-11/Machine-Learning-Projects.git
cd BigMart-Sales-Prediction
```

### 2. Install Dependencies
```
pip install -r requirements.txt
```

### 3. Run the Application
```
python app.py
```

### 4. Open in Browser
```
http://127.0.0.1:5000/
```

## How to Use
1. Open the app in the browser.
2. Enter 11 numerical features separated by commas.
3. Click Predict.
4. The predicted sales value will be displayed.

## Example Input
```
250,6.89,1,0.136428,13,193.9820,8,1997,2,0,1
```

