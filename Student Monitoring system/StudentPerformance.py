#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 20:58:14 2022

@author: subeidahassan
"""

import DAFunction as da #importing module created to use in this file
#importing packages
import matplotlib.pyplot as plt
import pandas as pd
import sqlite3


#creating function to view entire class results for selected test
def Class_results():
    """
    Prints class results for inputted Test.

    """
    print("Pick a test from: ")
    print("MockTest, FormativeTest_1, FormativeTest_2, FormativeTest_3, FormativeTest_4, SumTest")
    test = input("Enter Test: ")
    sqliteConnection = sqlite3.connect('ResultDatabase.db') 
    test_type = pd.read_sql(""" SELECT * 
                            FROM """ + test, sqliteConnection)
    sqliteConnection.close()
    test_type = test_type.drop(columns=['Started_on', 'Completed']) 
    print(test_type)

#creating function to view specific a student results for all questions on selected test 
def Student_performance():
    """
    Prints absolute and relative performance of wanted student \
and test with visulation.

    """
    student_id = input("Enter research ID: ")
    print("Pick a test from: ")
    print("MockTest, FormativeTest_1, FormativeTest_2, FormativeTest_3, FormativeTest_4, SumTest")
    test = input("Enter Test: ")
    sqliteConnection = sqlite3.connect('ResultDatabase.db')
    test_type = pd.read_sql(""" SELECT * 
                            FROM """ + test + 
                            """ WHERE research_id == """
                            + student_id, sqliteConnection) #sql statement to select specified table from db with conditions
    sqliteConnection.close()
    Absolute_performance = test_type.drop(columns=['research_id', 'Started_on', 'Completed'])
    print("Students absolute performance: ")
    print(Absolute_performance)
    sqliteConnection = sqlite3.connect('ResultDatabase.db')
    test_type2 = pd.read_sql(""" SELECT * 
                            FROM """ + test, sqliteConnection)
    sqliteConnection.close()
    test_type2 = test_type2.drop(columns=['research_id', 'Started_on', 'Completed'])
    average = test_type2.mean() #calculating mean value for all columns
    Relative_performance =  Absolute_performance - average #calculating relative performance
    print("Students relative performance: ")
    print(Relative_performance)
    Absolute_performance.plot(kind='bar')
    plt.title("Absolute Performance for " + test)
    plt.ylabel("Grade")
    plt.xlabel("Research ID: " + student_id)
    plt.show()
    Relative_performance.plot(kind = 'bar')
    plt.title("Relative Performance for " + test)
    plt.ylabel("Grade")
    plt.xlabel("Research ID: " + student_id)
    plt.show()
 
    
 
#creating function to compare overall performance on test for selected student & test
def Student_grade_performance():
    """
    Prints absolute and relative performance of overall grade for wanted \
student and test with visulation.

    """
    AllTestResults = da.AllTestResults_df()
    student_id = int(input("Enter research ID: ")) 
    print("Pick a test from: ")
    print("MockTest, FormativeTest_1, FormativeTest_2, FormativeTest_3, FormativeTest_4, SumTest")
    test = str(input("Enter Test: ")) 
    Absolute_performance  =  AllTestResults.loc[AllTestResults["research_id"] == student_id, test].item() #selecting grade value with column and row information
    print("Absolute_performance: ", Absolute_performance)
    avggrade = AllTestResults[test].mean() 
    Relative_performance = Absolute_performance  - avggrade 
    print("Relative_performance: ", Relative_performance)
    if Relative_performance < 0:
        print("Student performance: Below Average")
    else:
        print("Student performance: Above Average")
    Type = ['Absolute_performance', 'Relative_performance']
    score = [Absolute_performance, Relative_performance]
    plt.bar(Type, score, color = ['purple', 'green'])
    plt.title("Student Performance")
    plt.ylabel("Grade")
    plt.show()
