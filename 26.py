#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print(fact(5))
