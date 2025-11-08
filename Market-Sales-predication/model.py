# Importing required libraries
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics
import pickle

# Loading the dataset
big_mart_data = pd.read_csv('Train.csv')

# Displaying first 2 rows
big_mart_data.head(2)

# Checking shape of dataset (rows, columns)
big_mart_data.shape

# Viewing dataset information
big_mart_data.info()

# Checking missing values
big_mart_data.isnull().sum()

# Check duplicate values
big_mart_data.duplicated().sum()

# Filling missing Item_Weight values with mean
big_mart_data['Item_Weight'].fillna(big_mart_data['Item_Weight'].mean(), inplace=True)

# Checking mode of Outlet_Size column
big_mart_data['Outlet_Size'].mode()

# Calculating mode of Outlet_Size based on Outlet_Type
mode_of_outlet_size = big_mart_data.pivot_table(values='Outlet_Size', columns='Outlet_Type', aggfunc=lambda x: x.mode()[0])

# Identifying missing Outlet_Size rows
miss_values = big_mart_data['Outlet_Size'].isnull()

# Filling missing Outlet_Size values with respective Outlet_Type mode
big_mart_data.loc[miss_values, 'Outlet_Size'] = big_mart_data.loc[miss_values, 'Outlet_Type'].apply(lambda x: mode_of_outlet_size[x])

# Checking missing values again
big_mart_data.isnull().sum()

# Viewing statistical summary
big_mart_data.describe()

# Fixing inconsistent category names in Item_Fat_Content
big_mart_data.replace({'Item_Fat_Content': {'low fat':'Low Fat', 'LF':'Low Fat', 'reg':'Regular'}}, inplace=True)

# Label Encoding Categorical Columns
encoder = LabelEncoder()

big_mart_data['Item_Identifier'] = encoder.fit_transform(big_mart_data['Item_Identifier'])
big_mart_data['Item_Fat_Content'] = encoder.fit_transform(big_mart_data['Item_Fat_Content'])
big_mart_data['Item_Type'] = encoder.fit_transform(big_mart_data['Item_Type'])
big_mart_data['Outlet_Identifier'] = encoder.fit_transform(big_mart_data['Outlet_Identifier'])
big_mart_data['Outlet_Size'] = encoder.fit_transform(big_mart_data['Outlet_Size'])
big_mart_data['Outlet_Location_Type'] = encoder.fit_transform(big_mart_data['Outlet_Location_Type'])
big_mart_data['Outlet_Type'] = encoder.fit_transform(big_mart_data['Outlet_Type'])

# Separating Features and Target Column
X = big_mart_data.drop(columns='Item_Outlet_Sales', axis=1)
Y = big_mart_data['Item_Outlet_Sales']

# Splitting dataset into Training and Testing Data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

# Model Training (XGBoost Regressor)
regressor = XGBRegressor()
regressor.fit(X_train, Y_train)

# Predicting on Test Data
y_pred = regressor.predict(X_test)

# Checking model performance using R2 Score
metrics.r2_score(Y_test, y_pred)

# Sample Prediction Input (Example user input)
input = (250, 6.89, 1, 0.136428, 13, 193.9820, 8, 1997, 2, 0, 1)
new_input = np.asarray(input, dtype=float)
prediction = regressor.predict(new_input.reshape(1, -1))
print("Predicted Sales:", prediction)

# Saving the trained model into a pickle file
pickle.dump(regressor, open('model.pkl', 'wb'))
