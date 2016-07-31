#!/usr/bin/env python3
# coding=UTF-8
'''
    Created by Tracy on 2016/7/30
    Mail tracyliubai@gmail.com
'''
import networkx as nx
from queue import PriorityQueue


def k_shortest_paths(_paths, _source, _target, _top_k):
    '''
    :param paths: directed graph edge list e.g. [[from, to, weight],[]]
    :return: k shortest paths
    '''
    DG = nx.DiGraph()
    DG.add_weighted_edges_from([(u, v, w) for u, v, w in _paths])
    return yen_ksp(DG, _source, _target, _top_k)


def yen_ksp(G, src, tgt, top_K):
    from copy import deepcopy

    def getWeight(p, w=0):
        for i in range(len(p) - 1):
            w += G[p[i]][p[i + 1]]['weight']
        return w

    _cost, _path = nx.single_source_dijkstra(G, src, tgt)
    A = [_path[tgt]]
    costs = [_cost[tgt]]
    B = PriorityQueue()

    for k in range(1, top_K):
        _G = deepcopy(G)
        for i in range(len(A[k - 1]) - 1):
            spurNode = A[k - 1][i]
            rootPath = A[k - 1][:i]
            for path in A:
                if A[k - 1][:i + 1] == path[:i + 1] and _G.has_edge(path[i], path[i + 1]):
                    _G.remove_edge(path[i], path[i + 1])

            if len(rootPath) > 0 and spurNode != tgt:
                extra_edges = _G.edges(rootPath[len(rootPath) - 1])
                for ed in extra_edges:
                    _G.remove_edge(ed[0], ed[1])

            try:
                spurPathCost, spurPath = nx.single_source_dijkstra(_G, spurNode, tgt)
                spurPath = spurPath[tgt]
            except Exception as e:
                spurPath = []

            if len(spurPath) > 0:
                totalPath = rootPath + spurPath
                B.put((getWeight(totalPath), totalPath))
        if B.empty():
            break
        while not B.empty():
            cost, path = B.get()
            if path not in A:
                A.append(path)
                costs.append(cost)
                break
    return A, costs
