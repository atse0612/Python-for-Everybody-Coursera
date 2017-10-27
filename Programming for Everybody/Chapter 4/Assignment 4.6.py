# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:07:25 2017

@author: atse
"""

def computepay(hrs,rps):
    final_pay = 0.0
    hours = float(hrs)
    rate_per_hour = float(rps)
    if  hours>40:
        final_pay += 40 * float(rate_per_hour)
        hours -= 40
        final_pay += hours * rate_per_hour * 1.5
    else:
        final_pay += hours * rate_per_hour 
        
    return final_pay


hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
p = computepay(hrs,rate)
print(p)
