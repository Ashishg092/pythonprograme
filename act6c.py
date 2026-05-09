# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:35:44 2026

@author: Ashish Gaikwad
"""

try:
    with open("complaints.txt", "r") as file:
        print("List of Complaints:\n")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Complaint file not found.")