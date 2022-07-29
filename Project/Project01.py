# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 09:39:29 2022

@author: mselv
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\mselv\\Documents\\GitHub\\ECO5445\\'
git_path = 'C:/Users/jo585802/OneDrive - University of Central Florida/Documents/GitHub/ECO5445/' # Needed line to test data
os.chdir(git_path + '\\Project\\Data')
# Check that the change was successful.
os.getcwd()


mortgage_dataset = pd.read_csv("hmda_sw.csv", delimiter=',')

mortgage_dataset.rename(columns={'s13':'Applicant_race'},inplace=True)
mortgage_dataset.rename(columns={'s46':'D_to_I_Ratio_Total_Obligations'},inplace=True)
mortgage_dataset.rename(columns={'s45':'D_to_I_Ratio_Housing_Expenses'},inplace=True)
mortgage_dataset.rename(columns={'s27a':'Self-employed'},inplace=True)
mortgage_dataset.rename(columns={'s23a':'Marital_status'},inplace=True)
mortgage_dataset.rename(columns={'school':'Years_of_Education'},inplace=True)
mortgage_dataset.rename(columns={'s30a':'Applicant_Monthly_Employment_Income'},inplace=True)
mortgage_dataset.rename(columns={'s30c':'Coapplicant_Monthly_Employment_Income'},inplace=True)
mortgage_dataset.rename(columns={'s7':'Action_Taken'},inplace=True)
"""
Creating a new Dataframe which contains
the variables we want to use in our analysis
"""

###############################################################################
# Why did you choose these variables in particular? What information from the
# paper helped you decide?
###############################################################################

###############################################################################
# Didn't happen to notice that 999,999.4 is the designation for missing 
# numerical data. Summary statistics will be skewed.
###############################################################################

newData = mortgage_dataset[['Applicant_race','D_to_I_Ratio_Total_Obligations','D_to_I_Ratio_Housing_Expenses','Self-employed','Marital_status','Years_of_Education','Applicant_Monthly_Employment_Income','Action_Taken']]
newData.describe()

"""
Gathering summary statistics on different variables in order to 
see how a typical applicant would fall into these categories
"""

Applicant_Race = np.array(newData["Applicant_race"])

White_Applicants = np.count_nonzero(Applicant_Race == 5)
print(((White_Applicants/2380)*100),'percent of applicants are white')

DebttoIncome_Ratio = np.array(newData["D_to_I_Ratio_Total_Obligations"])

DtoI_Histogram = plt.hist(DebttoIncome_Ratio,bins=[12,20,28,36,44,52,60,68,76,84])
print(((DtoI_Histogram[0][2]/2380)*100),'percent of applicants have a Debt to Income Ratio that falls between 28 and 36')

Self_emp = np.array(newData["Self-employed"])

Self_Employed_Applicants = np.count_nonzero(Self_emp == 1)
print(((Self_Employed_Applicants/2380)*100),'percent of applicants are self-employed')

Married = np.array(newData["Marital_status"])

Married_Applicants = np.count_nonzero(Married == 'M')
print(((Married_Applicants/2380)*100),'percent of applicants are married')
"""
Creating a scatterplot to show the correlation between years of education
and monthly income
"""

Yrs_of_Education = np.array(newData["Years_of_Education"])
Monthly_Income = np.array(newData["Applicant_Monthly_Employment_Income"])

plt.xlim(0,40)
plt.scatter(Yrs_of_Education,Monthly_Income)

###############################################################################
# These plots do not provide details about what we are plotting
# They need context in order to understand.
###############################################################################

"""
Using the scatterplot for reference, you can see that the beginning
of the larger increases in monthly revenue correlate to surpassing 13 years of
education, meaning the individual pursued educational beyond high school.
"""

#Explanation of composition of sample and representative applicant

"""
As can be seen with the count functions used above, the vast majority 
of these applicants were white (2041 out of 2380). Most were also married 
and employed by others. Therefore, a representative applicant would be a white, 
married individual who has a great chance of being approved for his mortgage.
"""

#Probability of approval

Loan_Status = np.array(newData["Action_Taken"])

Loan_Originated = np.count_nonzero(Loan_Status == 1)
Approved_not_executed = np.count_nonzero(Loan_Status == 2)
Approved_Applicants = Loan_Originated + Approved_not_executed

Probability_of_Approval = ((Approved_Applicants/2380)*100)
print("The baseline probabilty of an individual being approved is", 
      Probability_of_Approval,"percent")
"""
Table for Number 6
"""

blackDenied = newData.loc[(newData['Applicant_race'] == 3) & (newData['Action_Taken'] == 3)]
blackDenied.describe() #count is 96

whiteDenied = newData.loc[(newData['Applicant_race'] == 5) & (newData['Action_Taken'] == 3)]
whiteDenied.describe() #count is 189

"""
Using the above calculations, you can fill out the remaining 
portions of the table.
"""

Approval_table = np.array([['Black',243,96,339],['White',1852,189,2041],['Total',2095,285,2380]])
print(Approval_table)

###############################################################################
# Missing column names
###############################################################################

"""
Number 7
"""

P_Approved_White = (((White_Applicants/2380)*(Approved_Applicants/2380))/
                    (White_Applicants/2380))

P_Denied_Black = (((1-(White_Applicants/2380))*(1-(Approved_Applicants/2380)))/
                  (1-(White_Applicants/2380)))


print(P_Approved_White)
print(P_Denied_Black)

###############################################################################
# What we were actually looking for is the probability that a person would be
# approved, given that we know they are white. So 1852/2041
###############################################################################