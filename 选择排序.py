#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

def select(list):
    for i in range(len(list)-1):
        min = i
        for j in range(i+1,len(list)):
            if list[j] < list[min]:
                list[j],list[min] = list[min],list[j]
                #temp = list[min]
                #list[min] = list[j]
                #list[j] = temp
        print('round ', i , ':',list)

a = [9,5,6,8,3,7,4,2,0,1]
select(a)
