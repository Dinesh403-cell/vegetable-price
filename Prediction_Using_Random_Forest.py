#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
dataset = pd.read_csv('D:\Forecasting_Internship\Only_few_dates.csv')
x = dataset.iloc[:, 0:8].values
y = dataset.iloc[:, 8].values
from sklearn.ensemble import RandomForestRegressor
  

regressor = RandomForestRegressor(n_estimators = 100, random_state = 0)

regressor.fit(x, y) 
Y_pred = regressor.predict(np.array([12,5,1,0,8,0,3160,33]).reshape(1, -1))  # test the output by changing values
# date, vegetable, festival, rainfall, season, inflation, avg. prev 5 days, arrival (in tons)
print ("Predicted Price is :- ", Y_pred)


# In[ ]:





# In[ ]:




