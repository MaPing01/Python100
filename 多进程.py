#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

from multiprocessing import Process
import os

def Test(name):
    print('run child process %s(%s)'  %(name,os.getpid()))

if __name__ ==  '__main__':
    print('parent process %s'% os.getpid())
    p = Process(target=Test,args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child and parent process end')

