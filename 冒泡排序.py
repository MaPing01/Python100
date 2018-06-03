#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

def Msort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                print(list)
        print(list)

a = [5,4,3,2,1,9,8,6,77,0,]
Msort(a)
