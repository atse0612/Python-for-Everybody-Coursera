# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 20:27:29 2017

@author: atse
"""

import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

lit = list()
while True:
    data = mysock.recv(512)
    lit.append(data)     
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
