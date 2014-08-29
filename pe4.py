#! /usr/bin/env python
# -*- encoding: utf-8 -*-

'''
http://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from
 the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
# Since May 23 2012

from itertools import product, combinations
from operator import mul
from time import time

lo = 100
hi = 1000
maxi = 0

# v1
# Stupid
st = time()


def panlindrom(lo, hi):
    global maxi
    for p in product(range(lo, hi), repeat=2):
        prod = str(mul(*p))
        if prod == prod[::-1] and int(prod) > maxi:
            maxi = int(prod)
    print maxi

panlindrom(lo, hi)
print 'Time used: {:.4f} s\n{}'.format(time() - st, '-'*20)

# v2
# Faster
# Compared to v1, we convert prod to string only when prod > maxi.
st = time()
for p in combinations(( i for i in range(hi-1, lo+1, -1) if i%10 ), 2):
    prod = mul(*p)
    if prod > maxi and not prod % 11:
        s = str(prod)
        if s == s[::-1]:
            maxi = prod

print maxi
print 'Time used: {:.4f} s\n{}'.format(time()-st, '-'*20)

# v3
# From http://www.s-anand.net/euler.html
# Not faster than v2
st = time()
n = 0
for a in xrange(999, 100, -1):
    for b in xrange(a, 100, -1):
        x = a * b
        if x > n:
            s = str(a * b)
            if s == s[::-1]:
                n = a * b

print n
print 'Time used: {:.4f} s\n{}'.format(time()-st, '-'*20)

# v3
# From http://www.s-anand.net/euler.html
# Not faster than v2
st = time()
n = 0
for a in xrange(999, 100, -1):
    for b in xrange(a, 100, -1):
        if (a%10 and b%10) and not (a%11 and b%11):
            x = a * b
            if x > n:
                s = str(a * b)
                if s == s[::-1]:
                    n = a * b

print n
print 'Time used: {:.4f} s\n{}'.format(time()-st, '-'*20)


# v4
#!/usr/bin/env python
st = time()
def is_palin(string):
    """Returns true if a string is a palindrome"""
    start, end = 0, len(string) - 1
    while end > start:
        if string[start] != string[end]:
            return False
        start += 1
        end -= 1
    return True

def palindrome():
    """Finds the largest palindrome that is the product of 2 3-digit numbers"""
    num1 = 999
    result_arr = []
    while num1 > 100:
        num2 = 990
        if num2 > num1:
            num2 = num1 - (num1 % 11)
        while num2 > 109:
            if is_palin(str(num1 * num2)):
                result_arr.append(num1 * num2)
            num2 -= 11
        num1 -= 1
    result_arr.sort()
    print result_arr[len(result_arr) - 1]

palindrome()
print 'Time used: {:.4f} s\n{}'.format(time()-st, '-'*20)

#v5
st = time()
maxnum = 0
for i in range(990, 99, -11):
    for j in range(999, i, -1):
        num = i * j
        if num <= maxnum:
            break
        else:
            strnum = str(num)
            if strnum == strnum[::-1]:
                maxnum = num
                break
print maxnum
print 'Time used: {:.4f} s\n{}'.format(time()-st, '-'*20)
