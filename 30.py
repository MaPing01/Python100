#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

x = input('please input a number: ')

if x == x[::-1]:
    print('%s是回文数' %x)
else:
    print('%s不是回文数' %x)
