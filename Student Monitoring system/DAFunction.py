#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Jan 11 21:16:19 2022

@author: subeidahassan
"""

import sqlite3
import pandas as pd

def save_tables_into_df():
    
    sqliteConnection = sqlite3.connect('ResultDatabase.db')

    MockTest_d = pd.read_sql("SELECT * FROM MockTest", sqliteConnection)
    FormativeTest_1_d = pd.read_sql("SELECT * FROM FormativeTest_1", sqliteConnection)
    FormativeTest_2_d = pd.read_sql("SELECT * FROM FormativeTest_2", sqliteConnection)
    FormativeTest_3_d = pd.read_sql("SELECT * FROM FormativeTest_3", sqliteConnection)
    FormativeTest_4_d = pd.read_sql("SELECT * FROM FormativeTest_4", sqliteConnection)
    SumTest_d = pd.read_sql("SELECT * FROM SumTest", sqliteConnection)

    sqliteConnection.close()
    
    global MockTest
    global FormativeTest_1
    global FormativeTest_2
    global FormativeTest_3
    global FormativeTest_4
    global SumTest
    
    MockTest = pd.DataFrame(MockTest_d)
    FormativeTest_1 = pd.DataFrame(FormativeTest_1_d)
    FormativeTest_2 = pd.DataFrame(FormativeTest_2_d)
    FormativeTest_3 = pd.DataFrame(FormativeTest_3_d)
    FormativeTest_4 = pd.DataFrame(FormativeTest_4_d)
    SumTest = pd.DataFrame(SumTest_d)
    

    return MockTest, FormativeTest_1, FormativeTest_2, FormativeTest_3, FormativeTest_3, SumTest

save_tables_into_df()

def AllTestResults_df():
    global AllTestResults
    #selecting columns id and grade for each df and updating
    MockTestgrade = MockTest[['research_id','Grade']]
    FormativeTest_1grade = FormativeTest_1[['research_id','Grade']]
    FormativeTest_2grade = FormativeTest_2[['research_id','Grade']]
    FormativeTest_3grade = FormativeTest_3[['research_id','Grade']]
    FormativeTest_4grade = FormativeTest_4[['research_id','Grade']]
    SumTestgrade = SumTest[['research_id', 'Grade']]
    
    #combining the dataframes 
    AllTestResults_d = MockTestgrade.merge(FormativeTest_1grade, 
    on ='research_id', how = 'outer').merge(
    FormativeTest_2grade, on = 'research_id', how = 'outer').merge(
    FormativeTest_3grade, on = 'research_id', how = 'outer').merge(
    FormativeTest_4grade, on = 'research_id', how = 'outer').merge(
    SumTestgrade, on = 'research_id', how = 'outer')

    AllTestResults_d = AllTestResults_d.fillna(0) #filling missing values
    
    #naming columns
    AllTestResults_d.columns = ['research_id', 'MockTest', 'FormativeTest_1', 
                              'FormativeTest_2', 'FormativeTest_3',
                              'FormativeTest_4', 'SumTest']
    AllTestResults = pd.DataFrame(AllTestResults_d)
    return AllTestResults

AllTestResults_df()

