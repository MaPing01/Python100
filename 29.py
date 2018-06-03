#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
x = int(input('please input a number : '))
a = x // 10000
b = x % 10000 //1000
c = x % 1000 // 1000
d = x % 100 // 10
e = x % 10

if a != 0:
    print('5位数',e,d,c,b,a)
elif b != 0:
    print('4位数',e,d,c,b,a)
elif c != 0:
    print('3位数',e,d,c,b,a)
elif d != 0:
    print('2位数',e,d,c,b,a)
elif e != 0:
    print('1位数',e,d,c,b,a)