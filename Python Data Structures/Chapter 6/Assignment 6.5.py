# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:11:42 2017

@author: atse
"""

text = "X-DSPAM-Confidence:    0.8475";
a = text[-6:]
b = float(a)
print(b)
text.find(":")
