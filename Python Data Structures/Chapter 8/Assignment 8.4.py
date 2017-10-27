# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

get = input('Please enter file name:')
handle = open(get)
text = list()
for line in handle:
	line = line.rstrip()
	line = line.split()
	for i in line:
		if i in text:
			continue
		else:
			text.append(i)
text.sort()
print(text)
