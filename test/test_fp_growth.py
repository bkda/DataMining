# coding=UTF-8
'''
    Created by Tracy on 2016/5/28
    Mail tracyliubai@gmail.com
'''
from Algorithm.FP_Growth import fp_growth
transactions = [
    [1, 2],
    [2, 3, 4],
    [1, 3, 4, 5],
    [1, 4, 5],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1],
    [1, 2, 3],
    [1, 2, 4],
    [2, 3, 5]
]
r=fp_growth(transactions,2)
for item,support in r:
    print('{:<10}'.format(str(item)),'{:<10}'.format(str(support)))