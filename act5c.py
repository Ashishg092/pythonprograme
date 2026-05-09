# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:32:13 2026

@author: Ashish Gaikwad
"""

purchases = ["apple", "banana", "apple", "orange", "banana", "apple"]
frequency = {}
for item in purchases:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1
print("Item frequency:", frequency)