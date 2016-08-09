#!/usr/bin/env python3
# coding=UTF-8
'''
    Created by Tracy on 2016/8/9
    Mail tracyliubai@gmail.com
'''
def hammingDistance(h1, h2):
    '''
    if h1 and h2 are string,they should have the same length
    :param h1: int or string 'da' & 'ad' or 3 & 1
    :param h2:
    :return: hamming distance between two vectors
    '''
    if isinstance(h1, int) and isinstance(h2, int):
        h, d = 0, h1 ^ h2
        while d:
            h += 1
            d &= d - 1
        return h
    elif isinstance(h1, str) and isinstance(h2, str):
        if len(h1) != len(h2):
            raise ValueError("Unequal length")
        return sum(e1 != e2 for e1, e2 in zip(h1, h2))
    else:
        raise ValueError("Mismatch")
