# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 09:37:46 2018
Output Format

Print  lines of output in the following order:
Print the mean on a new line, to a scale of  decimal place (i.e., , ).
Print the median on a new line, to a scale of  decimal place (i.e., , ).
Print the mode on a new line; if more than one such value exists, print the numerically smallest one.
Sample Input

10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
Sample Output

43900.6
44627.5
4978

@author: geoderek
"""
import numpy as np
X = np.array([[64630,11735,14216,99233,14470,4978,73429,38120,51135,67060]])
X = sorted(X[0])
print(np.mean(X))
print(np.median(X))
mode = 1
mode_val = 0
for x in X:
    num = (X == x).sum()
    if (num>mode):
        mode = num
        mode_val = x
if mode == 1:
    mode_val = np.min(X)
print(int(mode_val))
    