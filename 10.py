#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

#暂停一秒输出，并格式化当前时间。
import time

def func():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    print(time.time())
    start_time = time.time()
    time.sleep(1)
    end_time = time.time()
    print(time.time())
    print(time.localtime(time.time()))
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    print('run time is %s' %(end_time - start_time))
func()