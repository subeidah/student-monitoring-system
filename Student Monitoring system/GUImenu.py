#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 22:35:21 2022

@author: subeidahassan
"""

import testresults as tr
import StudentPerformance as sp
import underperformingStudent as up
import hardworkingStudents as hw
from tkinter import *


def say_hello():
    print ("hello")
def say_bye():
    print ("bye")
    window.destroy()


window=Tk()
window.title("Student Monitoring System")
window.geometry("250x250")

# Create all GUI components 

btnHello=Button(window,text="Hello",command=say_hello)
btnBye=Button(window,text="Exit",command=say_bye)
btnTestResults=Button(window, text = "students test results with visulisation",command = tr.Test_Results)
btnClassResults=Button(window, text = "class results for test",command = sp.Class_results)
btnStudentPerformance=Button(window, text = "student performance with visulisation",command = sp.Student_performance)
btnOverallPerformance=Button(window, text = "overall performance for test",command = sp.Student_grade_performance)
btnUnderPerforming=Button(window, text = "underperforming students",command = up.underperforming_students)
btnHwStudents=Button(window, text = "hardworking students",command = hw.hardworking_students)

# Define locations of the components 

btnHello.grid(column=0,row=0)
btnTestResults.grid(column=0,row=1)
btnClassResults.grid(column=0,row=2)
btnStudentPerformance.grid(column=0,row=3)
btnOverallPerformance.grid(column=0,row=4)
btnUnderPerforming.grid(column=0,row=5)
btnHwStudents.grid(column=0,row=6)
btnBye.grid(column=0,row=7)

window.mainloop()





