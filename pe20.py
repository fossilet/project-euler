#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''
# Since May 22 2012

###from projecteuler import calctime
#from projecteuler import calctime
import projecteuler as pe
import pprint

n = 100

# v1

from math import factorial

def v1(): 
    return sum(int(i) for i in str(factorial(n-1))[:-22:])
                                                #  ^^ 24 trailing zeros

# v2

def v2():
    f = 1
    for i in range(2, n):
        f *= i
        if not i%5:
            f //= 10
    return sum(int(i) for i in str(f))

#pprint.pprint(locals())
# Since python 3.0, the function attributes named func_X have been renamed to use the __X__ form, so there are no attribute such as func_name. See
#http://docs.python.org/py3k/whatsnew/3.0.html#operators-and-special-methods. 
# See PEP 3107 in http://docs.python.org/py3k/whatsnew/3.0.html#new-syntax.
for k, v in dict(locals()).items():
    if hasattr(v, '__annotations__'):
        print(v())
        pe.calctime('%s()'% k, 'from __main__ import %s' % k, 1000)
