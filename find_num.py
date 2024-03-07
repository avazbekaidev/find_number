# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 01:44:21 2024

@author: next nout
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint
def son_top_first():
    gamer=0;comp=0;
    print("men 1dan 10gacha son o'yladim uni toping")
    tax_son=int(input("taxminigiz :   "))
    son=randint(1,10)
    while True:
        gamer+=1
        if son > tax_son:
            print("Bu sondan katta")
            tax_son=int(input("Boshqa taxminigiz :   "))
        elif son<tax_son:
             print("Bu sondan kichik")
             tax_son=int(input("Boshqa taxminigiz :   "))
        else:
            print(f"Tabrikleman siz {gamer} urinishda topdiz")
            return gamer
def son_top_second():
    comp=0
    print("Endi siz son o'ylang men topaman!")
    input("Tayyor bosez hohlagan tugmani ezing")
    min=1;max=10
    while True:
        comp+=1
        tax_son=randint(min,max)
        javob=input(f"siz oyalgan  {tax_son} ? Tog'ri bosa (T),Bu sondan kotta bosa (+),kichik bosa(-)")
        if javob=="+":min=tax_son
        elif javob=="-":max=tax_son
        else:
            print(f"Men {comp} urinishda topdim")
            return comp

savol=True
while savol:
    a=son_top_first()
    b=son_top_second()
    if a<b:
        print(f"Bu safargi o'yinda siz yudtiz hisob {a}:{b}")
    elif a>b:
        print(f"Bu safargi o'yinda men yudtim hisob {a}:{b}")
    else:print("Durrang")
    savol=int(input("Yana o'ynashni hohlesizmi yes/no"))
        
        
            
            



