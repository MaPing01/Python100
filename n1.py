#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

import numpy as np
from pandas import Series,DataFrame
import pandas as pd
data1 = [1,2,3,4,5,6,7,8]
data2 = {'name':'andy','age':3,'score':100}
data3 = {'name':['andy','andy','kelly','sunday',''],
         'age':[11,14,12,13,13],
         'score':[80,80,90,100,60]}
a = np.arange(3)
b = np.array(data1)
c = Series(data2)
d = DataFrame(data3)
count_name = d['name'].value_counts()
count_score = d['score'].value_counts()
clean_name = d['name'].fillna('missing')
clean_name[clean_name==''] = 'Unknow'
print(a)
print(b)
print(c)
print(d)
print(d['name'])
print(clean_name)
print(d['score'])
print(count_name)
print(count_score)
