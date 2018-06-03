#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

def search1(list,t):
    for i in range(len(list)):
        if list[i] == t:
            print(i)
    print(-1)

def search2(list,t):
    i = 0
    while i < len(list):
        if list[i] == t:
            print(i)
        i += 1

a = [1,2,3,4,5]
search1(a,6)
search2(a,5)