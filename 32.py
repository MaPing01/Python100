#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

class MyError(Exception):
    pass
x = 0
try:
    if x == 0:
        raise MyError
except MyError as e:
    print('hello',e)
finally:
    print(x)