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

#冒泡排序
def bulubulu(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
a = [21,4,31,5,6]
bulubulu(a)
print(a)
