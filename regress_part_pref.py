# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:06:40 2018

@author: geoderek, w/ help from colleagues at austin hackathon
Following the guide to the Austin Hackathon, this script is meant to the focus on 
analyzing election data. Specifically, it starts with looking at linear and other 
regression models to score precincts for partisan preference.  
"""

# https://gis.stackexchange.com/questions/120571/iterate-through-a-shapefile
#import fiona
import geopandas as gpd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

#import pprint
#c = fiona.open(r"../Data/Wards2017_ED12toED16/Wards2017_ED12toED16.shp")
#pprint.pprint(c.schema)

wards_df = gpd.read_file(r"../Data/Wards2017_ED12toED16/Wards2017_ED12toED16.shp")
print(len(list(wards_df)))

#ward_df_for_model = wards_df[['BLACK18', 'USSREP14']]  #WHITE18
#x_values = ward_df_for_model[['BLACK18']].values
#y_values = ward_df_for_model[['USSREP14']].values 

ward_df_for_model = wards_df[['WHITE18', 'USSREP14']]  
x_values = ward_df_for_model[['WHITE18']].values
y_values = ward_df_for_model[['USSREP14']].values 


#train model on data
lm = LinearRegression()
lm.fit(x_values, y_values)

#https://tutorials.technology/tutorials/19-how-to-do-a-regression-with-sklearn.html
m = lm.coef_[0]
b = lm.intercept_
print(' y = {0} * x + {1}'.format(m, b))
# The mean squared error
print("Mean squared error: %.2f" % np.mean((lm.predict(x_values) - y_values) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % lm.score(x_values, y_values))

#
#visualise results
#plt.scatter(x_values, y_values)
plt.ylabel('reps')
plt.xlabel('blks')
plt.yscale('linear')
plt.xscale('linear')
#plt.scatter(x_values,y_values, c="pop")
#plt.scatter(x_values,lm.predict(x_values), c="pop")
plt.plot(x_values, lm.predict(x_values))
plt.show()


#=============================================================================
#This works for looping over features w/ fiona
#names = {}
#for feat in fiona.open(r"../Data/Wards2017_ED12toED16/Wards2017_ED12toED16.shp"):
#    print(feat['properties']['NAME'])
    