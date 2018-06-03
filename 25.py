#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#求1+2!+3!+...+20!的和.

def func(n):
    if n == 1:
        return 1
    return n * func(n-1)
result = 0
for i in range(1,21):
    result += func(i)
print(result)

