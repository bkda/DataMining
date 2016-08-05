#!/usr/bin/env python3
# coding=UTF-8
'''
    Created by Tracy on 2016/8/5
    Mail tracyliubai@gmail.com
'''
import math


def cosine_similarity(c1, c2):
    '''
    :param c1:  vector c1   (list) it can be integer or string list e.g. ['am','is']
    :param c2:  vector c2   (list)
    :return: cosine similarity
    :return: degrees
    '''
    '''
    integer list should have equal length
    string list will be calculated the frequency and generate list to get cosine similarity
    '''
    def cs(a, b):
        c = sum(a[i] * b[i] for i in range(len(a)))
        norm = lambda v: math.sqrt(sum(i * i for i in v))
        result = c / norm(a) / norm(b)
        return result, math.degrees(math.acos(result))

    if isinstance(c1[0], int):
        if len(c1) != len(c2):
            raise ValueError("Unequal length")
        return cs(c1, c2)
    elif isinstance(c1[0], str):
        d1, d2 = [], []
        for i in list(set(c1 + c2)):
            d1.append(c1.count(i))
            d2.append(c2.count(i))
        return cs(d1, d2)
