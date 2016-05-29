# coding=UTF-8
'''
    Created by Tracy on 2016/5/29
    Mail tracyliubai@gmail.com
'''
from Algorithm.Apriori import apriori
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
apriori(transactions, 2)