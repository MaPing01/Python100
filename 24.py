#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
x = 2
y = 1
s = []
for i in range(1,21):
    s.append(x/y)
    x, y = x, x+y
    x, y = y, x
print(sum(s))
