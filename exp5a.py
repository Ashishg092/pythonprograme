# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:20:50 2026

@author: Ashish Gaikwad
"""

student = {}
student["name"] = "Rahul"
student["age"] = 20
student["course"] = "Python"
print("Dictionary after adding elements:")
print(student)
student["age"] = 21
print("\nDictionary after updating a value:")
print(student)
del student["course"]
print("\nDictionary after deleting a key-value pair:")
print(student)