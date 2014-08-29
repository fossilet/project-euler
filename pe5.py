#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''
# Since May 23 2012

from itertools import count
div = 5

# v1 too slow: real    3m36.975s
def isok(n):
    for i in range(1, div+1):
        if n % i != 0:
            return False
    return True

for i in count(1):
    if isok(i):
        return i

# v2 too slow real	3m43.409s
# Demonstrate for ... else ...

for n in count(1):
    for i in range(1, div+1):
        if n % i != 0:
            break
    else:
        return n

# v3
# From http://www.s-anand.net/euler.html
def gcd(a,b):
    return b and gcd(b, a % b) or a

def lcm(a,b):
    return a * b / gcd(a,b)

n = 1
for i in xrange(1, div+1):
     n = lcm(n, i)

print n
