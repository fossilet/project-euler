#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://projecteuler.net/problem=13
'''
# Since Jun 2 2012

from projecteuler import calctime

# v1

def v1():
    print(str(sum(int(line) for line in open('pe13-chars')))[:10])

# v2

# XXX len(str(n*9))-1
def v2():
    print(str(sum(int(line[:12]) for line in open('pe13-chars')))[:10])

for i in range(1, 3):
    calctime('v%d()'%i, 'from __main__ import v%d'%i)
