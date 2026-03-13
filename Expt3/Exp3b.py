 # -*-calculate simple interest using a function with parameters-*-
"""
Created on Thu Mar 12 10:30:06 2026

@author: Ashish Gaikkwad 
"""

def simple_interest(principal, rate, time):
    
  si = (principal * rate * time) / 100
  
  return si
# Taking input from the user

p = float(input("Enter principal amount: "))

r = float(input("Enter rate of interest: "))

t = float(input("Enter time (in years): "))

interest = simple_interest(p, r, t)

print("Simple Interest is:",interest)
