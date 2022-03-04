# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 21:04:16 2022

@author: Sarah Tometzek
"""

import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm
import matplotlib.pyplot as plt

"""
Data Source:
    Unemployment: https://fred.stlouisfed.org/series/LMUNRRTTDEM156S
    Unfilled Jobs: https://fred.stlouisfed.org/series/LMJVTTUVDEQ647S
"""

""" Saving data and merging them into one DataFrame """
data_jobs = pd.read_csv("LMJVTTUVDEQ647S.csv")
data_unemployment = pd.read_csv("LMUNRRTTDEM156S.csv")
data_merged = pd.merge(data_unemployment, data_jobs, on="DATE", how="inner")
data_merged.columns = ["Date", "UR", "TUJV"]

""" Unemployment Rate and Total Unfilled Job Vacancies in Time """
fig,ax = plt.subplots()
ax.plot(data_merged["Date"], data_merged["UR"], color="red")
plt.xticks(rotation=90)
ax.set_xlabel("")
ax.set_ylabel("Unemployment Rate [%]",color="red",fontsize=14)
ax2=ax.twinx()
ax2.plot(data_merged["Date"], data_merged["TUJV"],color="blue")
ax2.set_ylabel("Total Unfilled Job Vacancies",color="blue",fontsize=14)
plt.xticks([0, 12, 24, 36, 48, 60, 72, 84, 96, 108, 
            120, 132, 144, 156, 168, 180, 192, 204])
plt.tight_layout()
plt.show()

""" Perform linear regression"""
linear_model = smf.ols(formula="UR ~ TUJV", data=data_merged)
linear_model_fit = linear_model.fit()
print(linear_model_fit.params)
print(linear_model_fit.summary())

""" Component-plus-residual plot """
fig_lr = sm.graphics.plot_ccpr(linear_model_fit, "TUJV")
fig_lr.tight_layout()
plt.show()

""" Beveridge Curve """
plt.plot(data_merged["UR"], data_merged["TUJV"], linewidth=5, color="k")
plt.grid()
plt.ylabel("Total Unfilled Job Vacancies")
plt.xlabel("Unemployment Rate [%]")
plt.tight_layout()
plt.show()
