#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
Common functions
'''
# Since Jun 2 2012

from timeit import Timer
from time import time


def calctime(stmt, setup, repeat=1):
    t = Timer(stmt, setup)
    print('µsec/pass: {:.4f}\n{}'.format(
                      1e6 * t.timeit(repeat) / repeat, '-' * 20))


class calctime1:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        st = time()
        rt = self.function(*args, **kwargs)
        print(time() - st)
        return rt
