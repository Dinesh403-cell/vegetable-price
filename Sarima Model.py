#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
data = pd.read_csv('D:\Forecasting_Internship\Sarima_Model.csv')
plt.figure(figsize=(15, 15))
data.plot()
data.index = pd.to_datetime(data['Date'])
data.drop(columns='Date',inplace=True)

from statsmodels.tsa.seasonal import seasonal_decompose
decompose_data = seasonal_decompose(data, model='additive',period=1)
decompose_data.plot();
plt.figure(figsize=(15, 15))
seasonality=decompose_data.seasonal
seasonality.plot(color='green')

import statsmodels.api as sm
mod = sm.tsa.statespace.SARIMAX(data,order=(1,1,1), seasonal_order=(1,1,1,12),enforce_stationarity=False, enforce_invertibility=False)
results=mod.fit()
print(results.summary())


# In[ ]:




