# -*- coding: utf-8 -*-
"""
Created on Sat May  9 14:09:22 2026

@author: Ashish Gaikwad
"""

n = int(input("Enter number: ")) 
fact = 1
for i in range(1, n + 1): 
 fact = fact*i
print("Factorial:", fact)