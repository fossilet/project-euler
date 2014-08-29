#! /usr/bin/env python

'''
http://projecteuler.net/problem=2

Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
# Since May 22 2012

mylim = 4000000

# v1
def fib(lim):
    fl = []
    a, b = 1, 2
    while a < lim:
        fl.append(a)
        a, b = b, a+b
    return fl

# v2

def fib_gen(lim):
    a, b = 1, 2
    while a < lim:
        yield a
        a, b = b, a+b

# v3

# Infinite generator
from itertools import takewhile

def fib_inf():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a+b

# v4 
# Memoization
memo = {0:0, 1:1}
def fib_memo(n):
    if not n in memo:
        memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

if __name__ == '__main__':
    # v1
    print sum( x for x in fib(mylim) if x%2 == 0 )

    # v2
    print sum( x for x in fib_gen(mylim) if not x%2 )

    # v3
    print sum( x for x in takewhile(lambda x: x <= mylim, fib_inf()) if not x%2 )

    # v4
    from itertools import count
    summ = 0
    for i in count():
        f = fib_memo(i)
        if f <= 4000000:
            if f%2 == 0:
                summ += f
            continue
        break
    print summ

    # v4
    i, n = 0, 0
    while fib_memo(i) <= 4000000:
        if not fib_memo(i) % 2:
            n += fib_memo(i)
        i += 1
    print n