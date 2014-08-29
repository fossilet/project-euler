#! /usr/bin/env python3
# encoding: utf-8

'''
http://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''
# Since May 22 2012

from projecteuler import calctime

n, a, b = 100000, 3, 5

# v1
def v1():
    summ = 0
    for i in range(n):
        if i%a == 0 or i%b == 0:
            summ += i
    return summ

# v2
# Generator expression faster than for loop
def v2():
    return sum( i for i in range(n) if i%a == 0 or i%b == 0 )

# v3
# Almost as fast as v2
def v3():
    return sum( i for i in range(n) if not i%a or not i%b )

# v4
# Almost as fast as v2
def v4():
    return sum( i for i in range(n) if not (i%a and i%b) )

# v5
# Time is O(1), the fastest
def v5():
    n = 999
    return sum((n//k*k+k)*(n//k)/2*v for k,v in {a:1, b:1, a*b:-1}.items())

if __name__ == '__main__':
    for i in range(1, 6):
        fname = 'v%d' % i
        print(locals()[fname]())
        calctime('%s()'% fname, 'from __main__ import %s' % fname, 50)
