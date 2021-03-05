# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 10:59:20 2021

@author: USER
"""
list_prime_number = list()
for i in range(1,11):
    for j in range(2,i):
       if i%j == 0:
           break
    else:
        list_prime_number.append(i)
print(*list_prime_number,sep=" ")