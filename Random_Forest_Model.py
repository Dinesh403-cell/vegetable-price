#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
dataset = pd.read_csv('D:\Forecasting_Internship\Only_few_dates.csv')
dataset.head()
X = dataset.iloc[:, 0:8].values
y = dataset.iloc[:, 8].values
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
# Feature Scaling

from sklearn.ensemble import RandomForestRegressor

regressor = RandomForestRegressor(n_estimators=1000, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print(regressor.score(X_test,y_test))
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# In[ ]:





# In[ ]:





# In[ ]:




