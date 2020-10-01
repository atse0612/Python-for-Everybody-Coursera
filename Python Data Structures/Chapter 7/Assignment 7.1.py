# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 09:12:55 2017

@author: atse
"""

# Use words.txt as the file name
fname = input("Enter file name: ")    #taking the user input and storing it in variable fname
fh = open(fname)      #opening the file stored in fname
a = fh.read()     #reading the file 
print(a.upper().rstrip())      #rstrip() removes trailing characters and upper method makes the strig in uppercase.
