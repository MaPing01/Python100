#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#判断101-200之间有多少个素数，并输出所有素数。
count = 0
for i in range(101,201):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        count += 1
        print('%d\t' %i,end='')
print()
print('count:%d' %count)
