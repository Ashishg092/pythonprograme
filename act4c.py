# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:29:36 2026

@author: Ashish Gaikwad
"""

# Program to remove duplicate mobile numbers from a contact list

# List of mobile numbers (with duplicates)
numbers = [9876543210, 9123456780, 9876543210, 9988776655, 9123456780, 9988776655]

# Removing duplicates using set()
unique_numbers = list(set(numbers))

# Displaying results
print("Original contact list:", numbers)
print("Contact list after removing duplicates:", unique_numbers)