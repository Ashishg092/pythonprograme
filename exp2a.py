# -*- coding: utf-8 -*-
"""
Created on Fri Feb 13 12:53:25 2026

@author: User
"""
year = int ( input (" ENTER  YEAR :" ))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0 ):

    print (" LEAP YEAR " )
 
else:

    print (" NOT A LEAP YEAR ")
