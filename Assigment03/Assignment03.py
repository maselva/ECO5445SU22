# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 20:25:36 2022

@author: mselv
"""

"""
Number 2
"""
import numpy as np

A = np.array([[1., 2., 3., 4.],
              [5., 6., 7., 8.],
              [9., 10., 11., 12.]])

"""
Number 3
"""

#I

A[1, 2]

#II

A[0]

#III

A[:,[1]]

#IV

A[1:]

#V

A[1:4, 2:4]

"""
Number 4
"""

B = np.array([[2.*A-8.]]) # Created a triple layered array (-2)
B = 2.*A-8.
#I

np.sum(B, axis=3)
np.sum(B, axis=1)
#II

np.sum(B, axis=2)
np.sum(B, axis=0)
#III


row_totals = B.sum() # Missing cummulative sum. Used sum instead (-5)
row_totals = np.sum(np.cumsum(B, axis=1),axis = 1)

print("Cumulative Sum of Row Values:", row_totals)


#IV

column_totals = B.sum() # Missing cummulative sum. Used sum instead (-5)
# The cumulative sum of column values
column_totals = np.sum(np.cumsum(B, axis=0),axis = 0)
print("Cumulative Sum of Column Values:", column_totals)

"""
Number 5
"""

#I

C = np.log(B)

#II

D = np.sqrt(B)

#III

E = np.square(B)

#IV

F = np.abs(B)

"""
Number 6
"""

M = np.array([[1., 20.],[1., -40.]])

N = np.array([[286.],[88.]])

np.dot(np.linalg.inv(M), N) # Which is the equilibrium price and which is quantity? (-4)
