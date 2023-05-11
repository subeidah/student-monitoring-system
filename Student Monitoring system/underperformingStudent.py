#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 23:51:12 2022

@author: subeidahassan
"""

import DAFunction as da


def underperforming_students():
    """
    Prints list of underperforming students.

    """
    AllTestResults = da.AllTestResults_df()
    underperformingstudents = AllTestResults.loc[(AllTestResults['SumTest'] >=1) & (AllTestResults['SumTest'] <=50) & 
                             ((AllTestResults['MockTest'] + AllTestResults['FormativeTest_1'] +
                               AllTestResults['FormativeTest_2'] + AllTestResults['FormativeTest_3'] +
                               AllTestResults['FormativeTest_4'])/5 <=50)] #selecting columns with conditions
    underperformingstudents = underperformingstudents.sort_values(by = 'SumTest', 
                                                                ascending=True) #sorting values from low to high
    underperformingstudents = underperformingstudents.loc[(underperformingstudents == 0).sum(axis=1) <=3] #filtering \
        #out disengaged students who did not attempt 3 or more tests by counting the number of 0 columns
    underperformingstudents['Lowest Grade'] = (underperformingstudents[underperformingstudents[['MockTest', 
                                                                                                'FormativeTest_1','FormativeTest_2', 'FormativeTest_3', 
                             'FormativeTest_4']] !=0]).min(axis = 1) #highlighting the lowest grade of formative tests for attempted tests, so non 0 values.
    print(underperformingstudents.round(2))
    


