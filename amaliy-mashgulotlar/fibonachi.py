# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 20:44:38 2021

@author: Admin
"""
def fibonachi(son):
    fib=[]
    fib.append(1)
    fib.append(1)
    i=2
    while i<son:
        fib.append(fib[i-1]+fib[i-2])
        i+=1
    return fib
print(fibonachi(13))