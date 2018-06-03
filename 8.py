#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#输出 9*9 乘法口诀表。

for i in range(10):
    print()
    for j in range(1,i+1):
        print('%d*%d=%2d\t' %(j,i,i*j), end='')