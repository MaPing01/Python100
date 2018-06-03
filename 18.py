#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

n = int(input('please input number:'))
times = int(input('please input times:'))
n1 = 0
result = 0
for i in range(0,times):
    n1 += n * (10 ** i)
    if i +1 == times:
        print('%d = ' %n1,end='')
    else:
        print('%d + ' % n1, end='')
    result += n1
print(result)