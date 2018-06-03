#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

user = {'a':1,'b':2,'c':1}
for key, value in user.items():
    print(key,value)
for key in user.keys():
    print(key)
for key in sorted(user.keys()):
    print(key)
for value in user.values():
    print(value)
for value in set(user.values()):
    print(value)
print(user.items())
print(user.keys())
print(user.values())