# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 17:07:30 2021

Assignment 1: Time series in economics

@author:     
"""
#import modules
import matplotlib.pyplot as plt
import numpy as np

#parameter definitions
number_of_assets = 20
number_of_periods = 10
initial_asset_value = 1000
price_volatility = 1 #must be positive value, 1 is standart, the more volatile market, the higher number

array_of_assets = [0] * number_of_assets #company owns 20 assets
value_per_timestep = [0] * number_of_periods #script simulates ten periods - this array saves average asset value for each period

#A1 : price development for each of the 20 asset
for n in range (0,number_of_assets):
    array_of_assets[n] = [initial_asset_value] * number_of_periods #assign initial value to n-th asset in each period
    for x in range (1,number_of_periods): #simulates value change of n-th asset in x-th time period
        array_of_assets[n][x] = np.random.normal(array_of_assets[n][x-1], price_volatility) #loc=x-1, scale=1.0 
        
#A3: calculating development of the investment capital of the ﬁrm 
for t in range (0,number_of_periods): # calculating average asset value for t-th period
    working_value = 0
    for a in range (0,number_of_assets): 
        working_value = working_value + array_of_assets[a][t]        
    value_per_timestep[t] = working_value/number_of_assets

# A2: plot settings
x = np.arange(1, number_of_periods+1, 1)

for s in range (0, number_of_assets):
    plt.plot(x, array_of_assets[s], label="Asset {number}".format(number = s+1))

plt.plot(x, value_per_timestep, linewidth=5, color="k", ls=('dotted'), label="Average IC")
plt.xticks(x)
plt.grid()
plt.legend(ncol=2, bbox_to_anchor=(1, 0.9))
plt.xlabel("Time")
plt.ylabel("Price")