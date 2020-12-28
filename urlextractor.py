# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 18:30:30 2020

@author: Mohit Mathur
"""

from urllib.request import urlopen

page=urlopen(input())
print(page.headers)

### To extract the source code

sourcecode= page.read()
print(sourcecode)