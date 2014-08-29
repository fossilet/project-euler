#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

# Solve http://projecteuler.net/problem=31
# Since May 22 2012

'''
In England the currency is made up of pound, £, and pence, p, and there are
eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
'''

from itertools import product
from operator import mul

COINS = (1, 2, 5, 10, 20, 50, 100, 200)


def combinations(x):
    '''Give an amount x, return the number of each coins in a list
    '''
    global COINS
    combs = []
    ways = 0
    for a in range(x / 1 + 1):
        for b in range(x / 2 + 1):
            for c in range(x / 5 + 1):
                for d in range(x / 10 + 1):
                    for e in range(x / 20 + 1):
                        for f in range(x / 50 + 1):
                            for g in range(x / 100 + 1):
                                for h in range(x / 200 + 1):
                                    if 1 * a + 2 * b + 5 * c + 10 * d + \
                                            20 * e + 50 * f + \
                                            100 * g + 200 * h == x:
                                        ways += 1
    return ways


def combinations1(x):
    '''The same as combinations, more beautiful and prevents SystemError here:
    http://www.newsmth.net/bbscon.php?bid=284&id=91367
    '''
    global COINS
    ways = 0
    r = (range(x / i + 1) for i in COINS)
    for t in product(*r):
        if sum(map(mul, t, COINS)) == x:
            ways += 1
    return ways


def _numfoo(n, rest):
    ''' http://www.newsmth.net/bbscon.php?bid=284&id=91477
    '''
    global COINS
    pounds = list(reversed(COINS))
    if n == 7:
        yield 1
        return
    for i in range(rest // pounds[n] + 1):
        for ele in _numfoo(n + 1, rest - i * pounds[n]):
            yield ele


def combinations2(x):
    '''Using recursion.
    '''
    return sum(1 for i in _numfoo(0, x))


def combinations3(x):
    '''Dynamic programming.
    '''
    coins = [1,2,5,10,20,50,100,200]
    ways = [1] + [0] * x
     
    for coin in coins:
        for i in range(coin, x + 1):
            ways[i] += ways[i - coin]

    return ways[x]


def combinations4(x):
    '''Brute force solution.
    '''
    ways = 0
    for a in range(x, -1, -200):
        for b in range(a, -1, -100):
            for c in range(b, -1, -50):
                for d in range(c, -1, -20):
                    for e in range(d, -1, -10):
                        for f in range(e, -1, -5):
                            for g in range(f, -1, -2):
                                ways += 1
    return ways
