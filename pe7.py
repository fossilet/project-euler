#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
# Since May 23 2012

from math import sqrt
from itertools import count

# v1 XXX very naive

num = 1
lim = 10001

def isprime(n):
   if n == 0 or n == 1:
      return False
   if n == 2:
       return True
   for i in range(2, int(sqrt(n)) + 2):
       if n%i == 0:
          return False
   return True
   
if __name__ == '__main__':
    pgen = ( i for i in count(2) if isprime(i) )
    while num < lim:
        pgen.next(),num
        num += 1
    print pgen.next()
