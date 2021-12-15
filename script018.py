#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 13:54:27 2021

Sample solution to Assignment 1:
    - create 20 random walks w/o drift
    - compute the average of those 
    - plot everything

@author: Torsten Heinrich
"""

""" Import modules"""
import numpy as np
import matplotlib.pyplot as plt

""" Define functions"""
def generate_random_walk(length):
    """
    Create one realization of the random walk
    Parameters
    ----------
    length : int
        length of random walk

    Returns
    -------
    random_walk : numpy ndarray
        Random walk realization
    """
    sample = np.random.choice([-1, 1], size=length)
    random_walk = np.cumsum(sample)
    return random_walk

def several_random_walks(number, length):
    """
    Create a list of random walks
    Parameters
    ----------
    number : int
        Number of random walks
    length : int
        Length of random walks

    Returns
    -------
    random_walks : list of numpy ndarrays
        List of random walks
    """
    random_walks = []
    for i in range(number):
        rw = generate_random_walk(length)
        random_walks.append(rw)
    return random_walks    

def several_random_walks_as_2d_array(number, length):
    """
    Create a list of random walks
    Parameters
    ----------
    number : int
        Number of random walks
    length : int
        Length of random walks

    Returns
    -------
    random_walks : list of numpy ndarrays
        List of random walks
    """
    random_walks = several_random_walks(number, length)
    """ Transform the list of arrays into a 2d array"""
    rw_array = np.asarray(random_walks)
    #rw_array = np.stack(random_walks)
    return rw_array   

def compute_average(array):
    """
    Compute the average of time series in a 2d numpy
    array.

    Parameters
    ----------
    array : numpy ndarray
        The 2d numpy array

    Returns
    -------
    rw_average : numpy array
        Array of averages
    """
    length = len(array[0])
    rw_average = np.zeros(length)
    for i in range(len(array)):
        rw_average += array[i]
    rw_average /= len(array)
    return rw_average
    
""" Main entry point"""
""" Create random walks"""
rw_array = several_random_walks_as_2d_array(20, 10000) 

""" Compute average"""
rw_average = compute_average(rw_array)
rw_average_2 = np.mean(rw_array, axis=0)    

""" Plot (first way)"""
fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
for i in range(len(rw_array)):
    ax[0][0].plot(np.arange(len(rw_array[i])), rw_array[i], color='k')
ax[0][0].plot(np.arange(len(rw_average)), rw_average, color='b')
ax[0][0].set_xlabel("Time")
ax[0][0].set_ylabel("Value of rw")
plt.show()

""" Plot (second way)"""
fig, ax = plt.subplots(nrows=1, ncols=1, squeeze=False)
ax[0][0].plot(rw_array.T, color="k")
ax[0][0].plot(np.arange(len(rw_average)), rw_average, color='b')
ax[0][0].set_xlabel("Time")
ax[0][0].set_ylabel("Value of rw")
plt.show()

    
    