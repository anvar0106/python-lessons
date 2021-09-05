# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:00:56 2021

@author: Anvar
"""
lugat = {
    'if':'shart tekshirish uchun',
    'else':'agar shart "false" bo`lsa',
    'elif':'yana shart tekshirish',
    'print':'chop etish operatori',
    'def':"funksiya e'lon qilish",
    'for':'takrorlash operatori'
    }
key = input("marhamat kalit so'zini kiriting:").lower()
check = lugat.get(key)
if check == None:
    print("Bunday kalit so'zi yo'q")
else:
    print(lugat[key])