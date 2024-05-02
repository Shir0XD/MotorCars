#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from pandas import DataFrame
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm
import statistics as st
import os

os.chdir('C:\\Users\\Shishir\\Desktop\\Desktop\\contact session 1\\code and datasets\\Pandas')
new_cars=pd.read_csv('new_cars.csv',sep=',',header=0, encoding="latin")

#Drop Duplicate rows
new_cars.drop_duplicates(subset=None, keep="first", inplace=True)

#Add new column for Points Making changes now
new_cars['Points']=1

#Outliers in Engine HP

Outhp = new_cars['Engine HP']
q1=Outhp.quantile(0.25) # finding the lower quartile value 
q3=Outhp.quantile(0.75) # finding the upper quartile value 
iqr = q3-q1  # Calculating the inter quartile range
print("q1=",q1)
print("q3=",q3)
print("iqr=",iqr)
upperfence = q3+(1.5*iqr) 
lowerfence = q1-(1.5*iqr)
print("upperfence=",upperfence)
print("lowerfence=",lowerfence)
a = [num for num in Outhp if num > upperfence]
b = [num2 for num2 in Outhp if num2 < lowerfence]
outlrs=a+b
print("Outliers = ",outlrs)

#Outliers in HighwayMPG
Outhmpg = new_cars['highway MPG']/2.352
q1=Outhmpg.quantile(0.25) # finding the lower quartile value 
q3=Outhmpg.quantile(0.75) # finding the upper quartile value 
iqr = q3-q1  # Calculating the inter quartile range
print("q1=",q1)
print("q3=",q3)
print("iqr=",iqr)
upperfence = q3+(1.5*iqr) 
lowerfence = q1-(1.5*iqr)
print("upperfence=",upperfence)
print("lowerfence=",lowerfence)
a = [num for num in Outhmpg if num > upperfence]
b = [num2 for num2 in Outhmpg if num2 < lowerfence]
outlrshmpg=a+b
print("Outliers = ",outlrshmpg)
new_cars.shape

delrow = new_cars[new_cars['highway MPG']>upperfence].index
new_cars.drop(delrow, inplace=True)
new_cars.shape

new_cars.loc[new_cars['Engine HP']<200,'Points'] += 1

indian=['MANUAL', 'AUTOMATIC', 'AUTOMATED_MANUAL']
new_cars.loc[new_cars['Transmission Type'].isin(indian),'Points'] += 1

indian_Manual=['MANUAL']
new_cars.loc[new_cars['Transmission Type'].isin(indian),'Points'] += 3

new_cars.loc[new_cars['Number of Doors']==4.0,'Points'] += 1

indian_cat=['High-Performance', 'Performance', 'Hatchback','Diesel','Crossover']
new_cars.loc[new_cars['Market Category'].isin(indian_cat),'Points'] += 1

indian_size = ['Compact','Midsize']
new_cars.loc[new_cars['Vehicle Size'].isin(indian_size),'Points'] += 1

indian_style = ['Sedan','4dr Hatchback','4dr SUV','Passenger Minivan','Cargo Minivan','Regular Cab Pickup','Extended Cab Pickup',
'Passenger Van']
new_cars.loc[new_cars['Vehicle Style'].isin(indian_style) ,'Points'] += 1

#converting new_cars['highway MPG'] from MPG to kmpl
new_cars['highway MPG']=new_cars['highway MPG']/2.352
new_cars.loc[new_cars['highway MPG']>14 ,'Points'] += 1

#converting new_cars['city MPG'] from MPG to kmpl
new_cars['city mpg']=new_cars['city mpg']/2.352
new_cars.loc[new_cars['city mpg']>10,'Points'] += 1

new_cars.groupby(['Make','Model'],as_index=False).agg({'Points':np.mean}).sort_values("Points",ascending=False).reset_index().head(5)


# In[ ]:




