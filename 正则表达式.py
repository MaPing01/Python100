#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

import re

str = input('please input a string :')

print(re.search('abc',str))
print(re.match('b',str))

