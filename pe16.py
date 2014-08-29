#! /usr/bin/env python3

'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

'''
# Since May 23 2012

from projecteuler import calctime1
# v1


def v1():
    return sum(int(i) for i in str(2**p))

# v2
# Slower


def v2():
    n = 1<<p
    s = 0
    while n > 0:
        s += n%10
        n //= 10
        # ^^ py3k
    return s

# v3
@calctime1
def v3(p):
    return sum(int(i) for i in str(1<<p))
'''
for i in range(1, 4):
    fname = 'v%d' % i
    print(locals()[fname]())
    calctime('%s()' % fname, 'from __main__ import %s' % fname)
'''

if __name__ == '__main__':
    p = 1000
    print(v3(p))
