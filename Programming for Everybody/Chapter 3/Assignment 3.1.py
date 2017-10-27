# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:03:50 2017

@author: atse
"""

try:
	h = input("please input your hour:")
	hour = float(h)
	r = input("please input your rate:")
	rate = float(r)
	if hour < 0:
		print("Please,input your positive numberic")
	elif rate < 0:
		print("Please,input your positive numberic")
	elif hour > 40:
		print("%.2f" % (40*rate+(hour-40)*1.5*rate))
	else:
		print("%.2f" % (hour*rate))
except:
		print("Please,input your numberic")
