# -*-nested loops to print a number pattern for n rows-*-
"""
Created on Fri Mar 13 13:33:19 2026

@author: Ashish Gaikwad
"""

n = int(input("Enter number of rows: "))
for i in range(1, n + 1):

    for j in range(1, i + 1):

        print(j, end=" ")

    print() 
