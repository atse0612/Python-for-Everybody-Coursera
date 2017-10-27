# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:04:59 2017

@author: atse
"""

score  = float(input("Enter a score between 0.0 and 1.0: "))
if score<0.0 or score>1.0:
    print("Error: Score out of range")
if score<0.6:
    print("F")
elif score>=0.6 and score<0.7:
    print("D")
elif score>=0.7 and score<0.8:
    print("C")
elif score>=0.8 and score<0.9:
    print("B")
elif score>=0.9:
    print("A")
    