# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 09:39:29 2022

@author: mselv
"""

import os
import pandas as pd

# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\mselv\\Documents\\GitHub\\ECO5445\\'
os.chdir(git_path + '\\Project\\Data\\')
# Check that the change was successful.
os.getcwd()

mortgage_dataset = pd.read_csv("hmda_sw.csv", delimiter=',')
