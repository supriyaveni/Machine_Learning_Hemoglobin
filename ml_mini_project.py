# -*- coding: utf-8 -*-
"""ML MINI PROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GGb6lVMSKjYDQkrHnZ4novgmzjniLcyv
"""



import pandas as pd
import numpy as np

df=pd.read_csv("/content/drive/MyDrive/smoking_driking_dataset_Ver01.csv")

df

from sklearn.preprocessing import LabelEncoder
label_encoder = LabelEncoder()
df['sex'] = label_encoder.fit_transform(df['sex'])
df['DRK_YN']=label_encoder.fit_transform(df['DRK_YN'])

"""#data preprocessing"""

df.isnull()

df.isnull().sum()

"""1.LINEAR REGRESSION

"""

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score,mean_absolute_error

subset_size = 5000
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
r2=r2_score(y_test,y_pred)
print(f'r2_score: {r2:.2f}')
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Absolute Error: {mae:.2f}')

"""2.DECISION TREE"""

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error

subset_size = 5000
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

dt_regressor = DecisionTreeRegressor(random_state=42)

dt_regressor.fit(X_train, y_train)

y_pred = dt_regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""3.RANDOM FOREST REGRESSION

"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score,mean_absolute_error

subset_size = 5000
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

random_forest_regressor = RandomForestRegressor(n_estimators=100,random_state=42)

random_forest_regressor.fit(X_train,y_train)

y_pred = random_forest_regressor.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)

print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""4.SUPPORT VECTOR MACHINE"""

from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

subset_size = 5000  # Adjust the size as needed
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler=StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

svr_model_subset = SVR(kernel='linear')  # You can try different kernels
svr_model_subset.fit(X_train_scaled, y_train)

y_pred = svr_model_subset.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""5.XG BOOST"""

from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

subset_size = 5000  # Adjust the size as needed
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

xgb_model=XGBRegressor(objective='reg:squarederror',random_state=42)
xgb_model.fit(X_train,y_train)

y_pred=xgb_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""6.LightGBM"""

from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

subset_size = 5000  # Adjust the size as needed
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

train_data = lgb.Dataset(X_train, label=y_train)
test_data = lgb.Dataset(X_test, label=y_test)

params = {
    'objective': 'regression',
    'metric': 'mse',
    'boosting_type': 'gbdt',  # Gradient Boosting Decision Tree
    'num_leaves': 31,
    'learning_rate': 0.05,
    'feature_fraction': 0.9
}

num_round = 100  # Number of boosting rounds
lgb_model = lgb.train(params, train_data, num_round, valid_sets=[test_data])

y_pred = lgb_model.predict(X_test, num_iteration=lgb_model.best_iteration)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""7.Ridge Regression"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

subset_size = 5000  # Adjust the size as needed
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)

alpha = 1.0  # Regularization strength (adjust as needed)
ridge_model = Ridge(alpha=alpha)
ridge_model.fit(X_train, y_train)

y_pred = ridge_model.predict(X_test_scaled)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""8.Lasso Regression"""

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

subset_size = 5000  # Adjust the size as needed
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test= scaler.transform(X_test)

alpha = 1.0
lasso_model = Lasso(alpha=alpha)
lasso_model.fit(X_train, y_train)

y_pred = lasso_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""9.K-Nearest Neighbors (KNN)"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.preprocessing import StandardScaler

subset_size = 5000  # Adjust the size as needed
subset = df.sample(n=subset_size, random_state=42)

x=subset.drop('hemoglobin',axis=1)
y=subset['hemoglobin']

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train= scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

k_neighbors = 5  # Number of neighbors (adjust as needed)
knn_model = KNeighborsRegressor(n_neighbors=k_neighbors)
knn_model.fit(X_train, y_train)

y_pred= knn_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae=mean_absolute_error(y_test,y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')
print(f'Mean Absolute Error:{mae:.2f}')

"""comparison"""

import pandas as pd
import matplotlib.pyplot as plt

# Results data
results_data = {
    'Algorithm': ['KNN', 'Las', 'Rid', 'LIG', 'XG', 'SVR', 'RF', 'DT', 'LR'],
    'Mean Squared Error': [1.59, 2.61, 1.36, 1.32, 1.42, 1.39, 1.33, 2.48, 1.36],
    'R-squared': [0.42, 0.05, 0.50, 0.52, 0.48, 0.49, 0.51, 0.09, 0.50],
    'Mean Absolute Error': [0.93, 1.26, 0.86, 0.85, 0.89, 0.85, 0.85, 1.20, 0.86]
}

# Create DataFrame
results_df = pd.DataFrame(results_data)
plt.figure(figsize=(15, 20))

# Print the table
print("Regression Algorithm Comparison:")
print(results_df)

# Plot results
plt.figure(figsize=(10, 6))

# Mean Squared Error
plt.subplot(2, 2, 1)
plt.bar(results_df['Algorithm'], results_df['Mean Squared Error'], color='skyblue')
plt.title('Mean Squared Error')
plt.ylabel('MSE')

# R-squared
plt.subplot(2, 2, 2)
plt.bar(results_df['Algorithm'], results_df['R-squared'], color='lightcoral')
plt.title('R-squared')
plt.ylabel('R-squared')

# Mean Absolute Error
plt.subplot(2, 2, 3)
plt.bar(results_df['Algorithm'], results_df['Mean Absolute Error'], color='lightgreen')
plt.title('Mean Absolute Error')
plt.ylabel('MAE')

plt.tight_layout(pad=3.0)
plt.show()