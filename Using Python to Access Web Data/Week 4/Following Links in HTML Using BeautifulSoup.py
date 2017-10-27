# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:12:49 2017

@author: atse
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
num = input('Enter count: ')
pos = input('Enter position: ')
print('Retrieving: ', url)
for times in range(int(num)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print('Retrieving: ', tags[int(pos)-1].get('href', None))
    url = tags[int(pos)-1].get('href', None)
