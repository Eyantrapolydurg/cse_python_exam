# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 11:18:14 2021

@author: USER
"""

def factorial(number):
    result_fac = 1
    for i in range(1,number+1):
         result_fac *= i
    return result_fac
   


print(factorial(0))
