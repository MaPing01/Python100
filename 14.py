#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

n = int(input('please input number:'))
print('%d = ' %n,end='')
while n not in [1]:
    for i in range(2,n+1):
        if n % i == 0:
            n //= i
            if  n == 1:
                print(i)
            else:
                print('%d *' %i, end='')
            break
