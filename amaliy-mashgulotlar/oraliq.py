# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:21:59 2021

@author: Admin
"""
def oraliq(min,max,step = 1):
    ans=[]
    while min<max:
      ans.append(min)
      min+=step
    return ans
print(oraliq(-51, 60,20))
