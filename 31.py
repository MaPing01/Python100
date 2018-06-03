#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

def func(value):
    try:
        print(int(value))
    except ValueError as e:
        print('input is not number :' ,e)
    else:
        print('success')
    finally:
        print('end')

func('xyz')