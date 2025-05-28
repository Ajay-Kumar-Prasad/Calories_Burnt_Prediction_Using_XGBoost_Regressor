# Calories_Burnt_Prediction_Using_XGBoost_Regressor

# Overview

This project aims to predict the number of calories burned during physical activities using the XGBoost Regressor algorithm. By analyzing user-specific data such as age, gender, height, weight, duration of exercise, and heart rate, the model provides accurate calorie burn predictions, assisting individuals in monitoring and optimizing their fitness routines.

# Dataset

The project utilizes two datasets:
exercise.csv: Contains exercise-related data including user ID, duration, heart rate, and body temperature.
calories.csv: Contains calorie information corresponding to each user ID.

These datasets are merged on the User_ID column to create a comprehensive dataset for analysis and modeling.

# Exploratory Data Analysis (EDA)

Key steps in EDA include:

Data Cleaning: Checked for missing values and inconsistencies.
Data Merging: Combined exercise.csv and calories.csv on User_ID.
Feature Engineering: Encoded categorical variables (e.g., gender) and created new features if necessary.
Visualization: Plotted distributions and relationships between variables to understand data patterns.

Male vs Female Data count
![alt text](/images/image.png)

Plotting Age vs Calorie Barplot
![alt text](/images/image-1.png)

Plotting Height vs Calorie Barplot
![alt text](/images/image-2.png)

Plotting Weight vs Calorie Barplot
![alt text](/images/image-3.png)

Plotting Heart_Rate vs Calorie Barplot
![alt text](/images/image-4.png)

Plotting Duration vs Calorie Barplot
![alt text](/images/image-5.png)

Plotting Body_Temp vs Calorie Barplot
![alt text](/images/image-6.png)

# Model Training
The XGBoost Regressor model is trained using the processed dataset.

# Model Evaluation
The model's performance is evaluated using the following metrics:
Mean Absolute Error (MAE)

Three regression models were evaluated based on their performance using Mean Absolute Error (MAE):

| Model                     | Mean Absolute Error (MAE) |
| ------------------------- | ------------------------- |
| **XGBoost Regressor**     | **1.47**                  |
| GradientBoostingRegressor | 2.70                      |
| AdaBoostRegressor         | 8.84                      |


✅ XGBoost Regressor demonstrated the best performance with the lowest MAE, making it the most suitable model for predicting calories burned.

# Project Structure
Calories_Burnt_Prediction_Using_XGBoost_Regressor/
├── calories.csv
├── exercise.csv
├── caloriesburntpredictor.ipynb
├── xgbregressor.pkl
├── README.md
└── LICENSE
