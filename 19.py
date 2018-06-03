#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
#程序分析：请参照程序Python 练习实例14。

#n = int(input('please input number:'))
for n in range(2,1001):
    l = [1]
    k = 1
    h = 0
    j = 0

    while n not in [1]:
        for i in range(2,n+1):
            if n % i == 0:
                n //= i
                l.append(i)
                break

    while j < len(l):
        h += l[j]
        k *= l[j]
        j += 1
    if h == k :
        print(l)