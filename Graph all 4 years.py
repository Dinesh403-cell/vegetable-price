#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import csv
  
x = []
y = []
  
with open('D:\Forecasting_Internship\Full_data.csv','r') as csvfile:
    lines = csv.reader(csvfile, delimiter=',')
    for row in lines:
        x.append(row[0])
        y.append(int(row[32]))
    plt.rcParams["figure.figsize"] = (50, 50)
plt.plot(x, y, color = 'g', linestyle = 'dashed',
         marker = 'o',label = "Potato Price")

plt.xticks(rotation = 100)
plt.xlabel('Date')
plt.ylabel('Potato Price (Per Kg)')
plt.title('Potato Price', fontsize = 20)
plt.grid()
plt.legend()
plt.show()


# In[ ]:




