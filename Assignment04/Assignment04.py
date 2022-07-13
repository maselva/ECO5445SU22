# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 20:18:02 2022

@author: mselv
"""

import numpy as np

n = 1000000

#Random data points across the square
data = np.random.uniform(-0.5, 0.5, size=(n, 2))

#Count points that are within 0.5 from center
inside = len(np.argwhere(np.linalg.norm(data, axis=1) <= 0.5)) # Boundary needed to be included (-10)

#Calculate pi
print(inside / n * 4)