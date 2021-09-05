# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:23:38 2021

@author: Admin
"""
def person(ism,familya,tyil,tjoy,e_mail='',tel=''):
    shaxs={
        'ism':ism,
        'familya':familya,
        'tyil':tyil,
        'yosh':2021-int(tyil),
        'tjoy':tjoy,
        'e-mail':e_mail,
        'tel':tel
        }
    return shaxs
kalit = 'yes'
k=1
shaxslar=[]
while True:
    print(f"marhamat {k}-fuqaro ma'lumotlarini kiriting : \n")
    ism = input("ismi : ")
    familya = input("familyasi : ")
    tyil = input("tu'gilgan yili : ")
    tjoy = input("tug'ilgan joyi : ")
    e_mail = input("e-mail pochtasi : ")
    tel = input("telefon raqami : ")
    shaxslar.append(person(ism, familya, tyil, tjoy,e_mail,tel))
    ans = input("yana ma'lumot kiritasizmi ? yes/no ")
    if ans=='no':
        break
    k+=1
print("\nshaxslar haqida quyidagi ma'lumotlar  :")
for shaxs in shaxslar:
    print(f"{shaxs['familya']} {shaxs['ism']} {shaxs['tyil']}-yilda\
          {shaxs['tjoy']}da tug'ilgan. Hozirda {shaxs['yosh']} yoshda\
              e-mail:{shaxs['e-mail']} tel:{shaxs['tel']}")
#print(shaxslar)
