#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

import random

def func():
    a = random.randint(0,5)
    yield a

f = func()
print(next(f))