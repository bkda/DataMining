#!/usr/bin/env python3
# coding=UTF-8
'''
    Created by Tracy on 2016/7/30
    Mail tracyliubai@gmail.com
'''
from Algorithm.ksp import k_shortest_paths
weightedEdge = [
    ['C', 'D', 3],
    ['C', 'E', 2],
    ['E', 'D', 1],
    ['E', 'F', 2],
    ['D', 'F', 4],
    ['E', 'G', 3],
    ['G', 'H', 2],
    ['F', 'G', 2],
    ['F', 'H', 1]
]
weightedEdge2=[
    [0,1,9],
    [0,2,7],
    [0,3,3],
    [2,1,1],
    [3,2,1],
    [1,4,13],
    [1,5,1],
    [2,5,5],
    [3,5,7],
    [3,6,2],
    [4,8,3],
    [5,8,2],
    [6,5,3],
    [6,8,9]
]
paths, costs = k_shortest_paths(weightedEdge2, 0, 8, 8)
for i in range(len(paths)):
    print('%5s   %s'%(costs[i],paths[i]))

paths, costs = k_shortest_paths(weightedEdge, 'C', 'H', 8)
for i in range(len(paths)):
    print('%5s   %s'%(costs[i],paths[i]))