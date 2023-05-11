#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 22:49:31 2022

@author: subeidahassan
"""

"""
Main App functions 
"""

import testresults as tr
import StudentPerformance as sp
import underperformingStudent as up
import hardworkingStudents as hw

def say_hello():
    print ("hello")
def say_bye():
    print ("bye")
    
def display_menu():
    """
    Building Menu Options
    
    """
    print ("\n")
    print ("*******************************************")
    print ("*------Student Monitoring System----------*")
    print ("*******************************************")
    print ("Please select an option below")
    print ("\t(h) say 'hello'")
    print ("\t(r) get students test results with visulisation")
    print ("\t(cr) get class results for test")
    print ("\t(p) student performance with visulisation")
    print ("\t(o) see students overall performance for test")
    print ("\t(u) see underperforming students")
    print ("\t(hw) see hardworking students")
    print ("\t(b) say 'bye'")

#################################################
#------------------Main-------------------------#
#################################################

#printing and executing menu options based on input into menu:

while True:
    display_menu()
    menuoption=input("\t\n:>") 
    if menuoption=="h":
        say_hello()
    elif menuoption=="b":
        say_bye()
        break 
    elif menuoption=="r":
          tr.Test_Results()
    elif menuoption=="cr":
          sp.Class_results()
    elif menuoption=="p":
          sp.Student_performance()
    elif menuoption=="o":
          sp.Student_grade_performance()
    elif menuoption=="u":
          up.underperforming_students()
    elif menuoption=="hw":
          hw.hardworking_students()
    else:
        print ("sorry we don't have that option")