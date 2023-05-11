#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 15:52:14 2022

@author: subeidahassan
"""


import matplotlib.pyplot as plt 
import DAFunction as da


def Test_Results():
    """
    Prints students grade for each test with visulation.

    """
    AllTestResults = da.AllTestResults_df()
    student_id = int(input("Enter research ID: ")) 
    Test_Results =  AllTestResults.loc[AllTestResults['research_id'] == student_id] #selecting column with inputted id
    print(Test_Results)
    Test_Results.plot(x = 'research_id', y = ['MockTest', 'FormativeTest_1', 
                             'FormativeTest_2', 'FormativeTest_3',
                             'FormativeTest_4', 'SumTest'], kind = 'bar', 
                     color=['pink', 'fuchsia', 'purple', 'indigo', 'blue', 'black']) 
    plt.title("Student Test Results")
    plt.ylabel("Grade/100")
    plt.xlabel("Research ID")
    plt.legend()
    plt.show()








