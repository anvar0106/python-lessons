# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 20:44:40 2021

@author: Admin
"""
def kv_kub(son):
    n=2
    while n<=10:
        if son % n == 0:
            print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
        n+=1
son = int(input("sonni kirting : "))
kv_kub(son)