# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:34:11 2021

@author: Anvar
"""

#odam={'ism':'diyorbek','yoshi':17,"millati":"o'zbek"}
#print(f"Fuqaro {odam['ism'].title()}\
#      millati {odam['millati']} \
#      yoshi {odam['yoshi']} da")
# lug'at yaratish
en_uz={
       'apple':'olma',
       'car':'mashina',
       'bread':'non',
       'milk':'sut',
       'hello':'salom',
       'book':'kitob'
       }
# lug'atga yangi so'zlar qo'shish
en_uz['good']='yaxshi'
en_uz['bad']='yomon'
print(en_uz)
# lug'atdan so'zlar o'chirish 
del en_uz['bad']
print(en_uz)
# lug'atdan bitta elementni olish
word=en_uz.get('orange','bunday so`z mavjud emas')
print(word)