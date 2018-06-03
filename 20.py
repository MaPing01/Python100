#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping
#一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
tour = []
hei = []
heigh = 100
for time in range(1,11):
    if time == 1:
        tour.append(heigh)
    else:
        tour.append(2*heigh)
    heigh = heigh/2
    hei.append(heigh)
print(tour,hei)
print(sum(tour),hei[9])