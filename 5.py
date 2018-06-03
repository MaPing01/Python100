#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping
#输入三个整数x,y,z，请把这三个数由小到大输出。
arry = []
for i in range(3):
    arry.append(int(input('please enter a number:')))

    l = len(arry)
    for j in range(l):
        for k in range(j+1,l):
            if arry[j] > arry[k]:
                temp = arry[j]
                arry[j] = arry[k]
                arry[k] = temp
print(arry)