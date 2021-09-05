# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 23:55:44 2021

@author: Admin
"""
def ism_yasash(ism,familya,otasining_ismi=''):
    if otasining_ismi:
        ans=f"{familya} {ism} {otasining_ismi}"
    else:
        ans=f"{familya} {ism}"
    return ans.title()
talaba1 = ism_yasash('mirjalol',"ahmedov","davronovich")
talaba2 = ism_yasash(familya='hasanov',ism='temur')
print(f'{talaba1} va {talaba2}')