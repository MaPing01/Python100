#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

def Min(list):
    min = 0
    for i in range(1,len(list)):
        if list[i] < list[min]:
            min = i
    return min

a = [6,2,1,4,5]
print(Min(a))