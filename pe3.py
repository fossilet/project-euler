#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://projecteuler.net/problem=3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
# Since May 31 2012

# v1

from p7 import isprime
from math import sqrt

def factor(n):
    for i in range(2, int(sqrt(n)+2)):
        if not n%i and isprime(i):
            yield i

# v2
# From http://www.s-anand.net/euler.html
# Very fast

n = 600851475143
i = 2
while i*i < n:
    while n%i == 0:
        n /= i
        #print n,
    #print i
    i += 1

if __name__ == '__main__':
    print max(factor(600851475143))
    print n
