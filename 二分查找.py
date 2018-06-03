#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

def search(list,t):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        if list[mid] < t:
            low = mid + 1
        elif list[mid] > t:
            high = mid -1
        elif list[mid] == t:
            return mid
    return -1
a = [1,2,3,4,5]
print(search(a,6))