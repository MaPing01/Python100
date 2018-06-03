#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping
import time

def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        print('start time :',start_time)
        func()
        end_time = time.time()
        print('end time :',end_time)
        return end_time - start_time
    return wrapper

@timer
def test():
    time.sleep(3)

print(test())

