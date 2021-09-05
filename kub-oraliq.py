# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 14:13:47 2021

@author: Admin
"""
def tub(a,b):
    ans = []
    k=0
    while a<=b:
        for i in range(a):
            if a % (i+1)==0:
                k+=1
        if k==2:
            ans.append(a)
        a+=1
        k=0
    return ans
print(tub(2,18000))