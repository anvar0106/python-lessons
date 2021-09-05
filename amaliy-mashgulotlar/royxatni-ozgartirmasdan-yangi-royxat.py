# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 23:14:50 2021

@author: Admin
"""
def ismlar(ism):
    ans = []
    for name in ism:
        ans.append(name.title())
    return ans
nomlar = ['anvar','sarvar','diyorbek','mahmud']
print(ismlar(nomlar[:]))
print(nomlar)
