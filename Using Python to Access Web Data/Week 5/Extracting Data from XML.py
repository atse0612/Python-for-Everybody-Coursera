# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:43:48 2017

@author: atse
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print ('Retrieving ', url)
html = urllib.request.urlopen(url, context=ctx).read()
print ('Retrieved', len(html), 'characters')
tree = ET.fromstring(html)
print ('Count: ',len(tree.findall('.//count')))
total = 0
for r in tree.findall("./comments/comment"):
    total += int(r.find('count').text)
print ('Sum: ', total)
