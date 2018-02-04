# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:06:40 2018

@author: geoderek, w/ help from colleagues at austin hackathon
Following the guide to the Austin Hackathon, this script is meant to the focus on 
analyzing election data. Specifically, it starts with looking at linear and other 
regression models to score precincts for partisan preference.  
"""

# https://gis.stackexchange.com/questions/120571/iterate-through-a-shapefile
import geopandas as gpd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
pylab.rcParams['figure.figsize'] = 18, 16

wards = gpd.read_file(r"../../Data/Wards2017_ED12toED16/Wards2017_ED12toED16.shp")
#print(list(wards_df))

ward_attribs = wards[['USSREP14','WHITE18', 'BLACK18', 'HISPANIC18', 'ASIAN18', 'AMINDIAN18', 'PISLAND18', 'OTHER18', 'OTHERMLT18']]  
y = ward_attribs[['USSREP14']]
X = ward_attribs.drop('USSREP14', axis=1)

lm = LinearRegression()
lm.fit(X, y)

regression_model = LinearRegression()
regression_model.fit(X, y)
print(regression_model)
for idx, col_name in enumerate(X.columns):
    print("The coefficient for {} is {}".format(col_name, regression_model.coef_[0][idx]))

intercept = regression_model.intercept_[0]
print("The intercept for our model is {}".format(intercept))

wards.plot(column='USSREP12', cmap='OrRd', scheme='quantiles')
plt.xlim([-89.4, -89.4])
plt.ylim([43.05, 43.05]);
