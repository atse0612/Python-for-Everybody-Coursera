# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:12:55 2017

@author: atse
"""

# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a = fh.read()
print(a.upper().rstrip())