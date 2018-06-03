#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

from multiprocessing import Process,Queue
import os,random,time

def Write(q):
    print('process to write: %s'%os.getpid())
    for value in ['A','B','C','D']:
        print('put value %s to queue'%value)
        q.put(value)
        time.sleep(random.random())

def Read(q):
    print('process to read: %s'%os.getpid())
    while True:
        value = q.get(True)
        print('get %s from queue'%value)

if __name__ == '__main__':
    q = Queue()
    pw = Process(target=Write,args=(q,))
    pr = Process(target=Read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()