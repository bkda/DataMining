#!/usr/bin/env python3
# coding=UTF-8
'''
    Created by Tracy on 2016/8/5
    Mail tracyliubai@gmail.com
'''
from Algorithm.CosineSimilarity import cosine_similarity

a = [1, 2, 2, 1, 1, 1, 0]
b = [1, 2, 2, 1, 1, 2, 1]

# a = ['i', 'am', 'a', 'good', 'boy', 'i', 'write', 'code']
# b = ['a', 'good', 'boy', 'can', 'write', 'code']

similarity, angle = cosine_similarity(a, b)
print(similarity, angle)
