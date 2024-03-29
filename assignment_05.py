# -*- coding: utf-8 -*-
"""Assignment-05.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eTZ7i5MLvlkNXz0y0Ug-7yItZH5z3-Xm
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Step 1: Load the Data
data = pd.read_csv("/content/gld_price_data.csv")

# Step 2: Drop the 'Date', 'EUR/USD' columns
data = data.drop(['Date', 'EUR/USD'], axis=1)

# Step 3: Split the Data
X = data.drop(['GLD'], axis=1)  # Features excluding 'GLD'
y = data['GLD']  # Target variable 'GLD'

# Step 4: Split into Training and Testing Sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 5: Train a Regression Model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make Predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate the Model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f'MAE: {mae}')
print(f'MSE: {mse}')
print(f'RMSE: {rmse}')
print(f'R^2 Score: {r2}')