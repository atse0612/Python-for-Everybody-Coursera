# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:10:37 2017

@author: atse
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
html = urlopen('  http://py4e-data.dr-chuck.net/comments_41649.html', context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
sum = 0
coun = 0
print('Enter - ')
for tag in tags:
    coun += 1    
    sum += int(tag.contents[0])
print('Count', coun, '\nSum', sum)
