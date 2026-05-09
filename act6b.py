# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:34:49 2026

@author: Ashish Gaikwad
"""

with open("attendance.txt", "a") as f:
    for i in range(3):
        name = input("Enter student name: ")
        status = input("Present/Absent: ")
        f.write(name + " - " + status + "\n")

print("Attendance recorded successfully.")