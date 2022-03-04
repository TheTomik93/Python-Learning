# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 22:12:33 2022

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

"""Parameter definition"""
initSize = 10000
numberOfFirms = 10000
timeSteps = 10
chosenTimeStep = timeSteps - 1

alfaLow = 0.8
alfaHigh = 1.2
betaLow = 0
betaHigh = 10000

plotBins = 100

"""Initialization of empty lists for storing values"""
firmsList = [0] * numberOfFirms
valuesOnChosenTimestep = []

"""Simulating values of all companies in all timesteps"""
for x in range(numberOfFirms):
    firmsList[x] = [initSize]*timeSteps
    print("Firm " + str(x) + " initialized, simulating values:")
    
    for t in range(timeSteps-1):
        firmsList[x][t+1] = (firmsList[x][t] 
                             * np.random.uniform(alfaLow, alfaHigh) 
                             + np.random.uniform(betaLow, betaHigh))
        print(firmsList[x][t+1])

"""Saving company values in the chosen timestep for plotting purposes"""
for i in range(numberOfFirms):         
    valuesOnChosenTimestep.append(firmsList[i][chosenTimeStep])

"""Plotting histograms of company values"""      
fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
ax[0][0].hist(valuesOnChosenTimestep, plotBins, color='gold', edgecolor='black',
             alpha=1, rwidth=None)
ax[0][0].set_xlabel("Company value")
ax[0][0].set_ylabel("Number of companies (frequency)")
plt.title("Normal-normal")
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
ax[0][0].hist(valuesOnChosenTimestep, plotBins, color='dodgerblue', 
              edgecolor='black', alpha=1, rwidth=None)
ax[0][0].set_xlabel("Company value")
ax[0][0].set_ylabel("Number of companies (frequency)")
ax[0][0].set_yscale("log")
plt.title("Normal-log")
plt.show()

fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
ax[0][0].hist(valuesOnChosenTimestep, plotBins, color='orchid', edgecolor='black', 
             alpha=1, rwidth=None)
ax[0][0].set_xlabel("Company value")
ax[0][0].set_ylabel("Number of companies (frequency)")
ax[0][0].set_xscale("log")
plt.title("Log-normal")
plt.show()
        
fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
ax[0][0].hist(valuesOnChosenTimestep, plotBins, color='limegreen', 
              edgecolor='black', alpha=1, rwidth=None)
ax[0][0].set_xlabel("Company value")
ax[0][0].set_ylabel("Number of companies (frequency)")
ax[0][0].set_yscale("log")
ax[0][0].set_xscale("log")
plt.title("Log-log")
plt.show()     