import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
import os

# Load the data
df = pd.read_csv('insurance_data.csv')
x = df[['age']]
y = df['bought_insurance']

# Train the logistic regression model
model = LogisticRegression()
model.fit(x, y)

# Create models directory and save the model
os.makedirs('models', exist_ok=True)
with open('models/insurance_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Logistic Regression model trained and saved successfully.")
print(f"Model coefficients: {model.coef_}")
print(f"Model intercept: {model.intercept_}")
