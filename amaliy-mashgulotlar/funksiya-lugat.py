# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 00:07:42 2021

@author: Admin
"""
def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rangi':rangi,
        'korobka':korobka,
        'yil':yili,
        'narh':narhi
        }
    return avto
avto1 = avto_info('GM','Nexia3','oq','mexanika',2019)
avto2 = avto_info('BMW','BMW X6','qora','avtomat',2021,67000)
avtolar = [avto1,avto2]
for car in avtolar:
    if car['narh']:
        narh = car['narh']
    else:
        narh = "noma'lum"
    print(f"{car['rangi']} {car['model']} narxi : {narh}")