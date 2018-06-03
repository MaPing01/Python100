#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

score = int(input('please input your score: '))
if score >= 90:
    result = 'A'
elif 60 < score < 89:
    result = 'B'
elif score < 60:
    result = 'C'
print('The result is %s' %result)