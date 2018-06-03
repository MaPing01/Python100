#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

import time

def func():
    start_time = time.time()
    time.sleep(1)
    end_time = time.time()
    print('run time is %s' %(end_time - start_time))
func()