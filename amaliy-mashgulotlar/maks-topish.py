# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:57:11 2021

@author: Admin
"""
def max_topish(son1,son2,son3):
    maks=son1
    if maks<son2:
        maks=son2
    if maks<son3:
        maks=son3
    return maks
print(max_topish(25,-8,-7))
