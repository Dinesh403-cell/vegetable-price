#!/usr/bin/env python
# coding: utf-8

# In[16]:


import numpy as np 
import pandas as pd 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
dataset = pd.read_csv('D:\Forecasting_Internship\Only_few_dates.csv')
print(dataset.corr())

X = df.drop('Potato Price (Rounded)', 1)
y = df['Potato Price (Rounded)']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
from sklearn.decomposition import PCA

pca = PCA()
X_train = pca.fit_transform(X_train)
X_test = pca.transform(X_test)
explained_variance = pca.explained_variance_ratio_
print('\n')

print(explained_variance)


# In[ ]:




