#!usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Ma Ping

class A():
    def __init__(self):
        self.name = 'Aname'
    def go(self):
        print('a go a')

class B():
    def go(self):
        #super(B, self).go()
        print('b go b')
class C(A):
    def go(self):
        super(C, self).go()     #python2 and python3
        print('c go c')
class D(B,A):
    def __init__(self):
        super(D, self).__init__()
        self.age = 'Dage'
    def go(self):
        super().go()           #python3
        print('d go d')

#b = B()
d = D()
#b.go()
d.go()
print(d.name,d.age)