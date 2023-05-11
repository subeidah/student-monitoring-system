#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 23:52:15 2022

@author: subeidahassan
"""

import DAFunction as da
import pandas as pd


def hardworking_students():
    """
    Prints list of hardworking students.

    """
    AllTestResults = da.AllTestResults_df()
    sumtestresults = AllTestResults[["research_id", "SumTest"]] #selecting wanted columns
    studentrates =pd.read_csv("StudentRate.csv") #reading csv file
    studentrates = studentrates[['research id', 'What level programming knowledge do you have?']]
    studentrates.columns = ['research_id', 'Rates'] #renaming columns
    hw_students = sumtestresults.merge(studentrates, on ='research_id', how = 'outer') #combining dfs
    hw_students = hw_students.loc[hw_students['SumTest'] >= 60] #selecting only students who acheived 60 or more for sumtest
    hw_students = (hw_students.loc[hw_students['Rates'].isin(['Below beginner','Beginner'])]) #selecting below beginner or beginner students.
    hw_students = hw_students.sort_values(by = 'SumTest', ascending=False) #sorting sum test results highest to lowest. Hardest working student first.
    print(hw_students.round(2))    
