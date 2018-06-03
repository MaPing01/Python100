#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#输入某年某月某日，判断这一天是这一年的第几天？

year = int(input('请输入年：'))
month = int(input('请输入月：'))
day = int(input('请输入日：'))

days = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < month <= 12:
    sum = days[month - 1]
sum = sum + day
#普通年能被4整除但是不能被100整除；世纪年能被400整除的是闰年
if (year % 400 == 0)  or ((year % 4 == 0) and (year % 100 != 0)):
    if month > 2:
        sum += 1
print('是%d天' %sum)