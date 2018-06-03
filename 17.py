#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string

s =  str(input('please input string:'))
digit = 0
space = 0
alpha = 0
others = 0
for i in range(len(s)):
    c = s[i]
    if c.isalpha():
        alpha += 1
    elif c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    else:
        others += 1
print('digit = %d, space = %d, alpha = %d, other = %d' %(digit,space,alpha,others))

