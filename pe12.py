#! /usr/bin/env python3

"""
http://projecteuler.net/problem=12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:
     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?


Wed Apr 30 11:44:56 CST 2014
"""


def triangle(n):
    """Return the nth triangle number."""
    assert n > 0
    return sum(range(n + 1))


def num_factors(n):
    """Return the number of factors of n"""
    assert n > 0
    # TODO: how to find factors?

if __name__ == '__main__':
    print(triangle(1))
    print(triangle(7))