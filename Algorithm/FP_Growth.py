# coding=UTF-8
'''
    Created by Tracy on 2016/5/26
    Mail tracyliubai@gmail.com
'''
from collections import defaultdict, namedtuple


class FP_Node:
    def __init__(self, tree, item, count=1):
        self.tree = tree
        self.item = item
        self.count = count
        self._parent = None
        self._neighbor = None
        self._children = {}

    def add(self, child):
        '''
        :param child: _children dict add child & parent -> self
        :return:
        '''
        if child.item not in self._children:
            self._children[child.item] = child
            child.parent = self

    def search(self, item):
        try:
            return self._children[item]
        except KeyError:
            return None

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, item):
        self._parent = item

    @property
    def neighbor(self):
        return self._neighbor

    @neighbor.setter
    def neighbor(self, item):
        self._neighbor = item

    @property
    def root(self):
        return self.item is None and self.count is None

    @property
    def leaf(self):
        return len(self._children) == 0

    def increase(self):
        self.count += 1


class FP_Tree:
    Route = namedtuple('Route', 'head tail')

    def __init__(self):
        self._root = FP_Node(self, None, None)
        self._route = {}

    @property
    def root(self):
        return self._root

    def add(self, transaction):
        point = self._root
        for i in transaction:
            next_node = point.search(i)
            if next_node:
                next_node.increase()
            else:
                next_node = FP_Node(self, i)
                point.add(next_node)
                self.update_route(next_node)

            point = next_node

    def update_route(self, point):
        '''
        :param point:
        :return:
        '''
        try:
            route = self._route[point.item]
            route[1].neighbor = point
            self._route[point.item] = self.Route(route[0], point)
        except KeyError:
            self._route[point.item] = self.Route(point, point)

    def items(self):
        for i in self._route.keys():
            yield i, self.nodes(i)

    def nodes(self, item):
        try:
            node = self._route[item][0]
        except KeyError:
            return
        while node:
            yield node
            node = node.neighbor

    def prefix_paths(self, item):
        def collect_path(node, path):
            while node and not node.root:
                path.append(node)
                node = node.parent
            path.reverse()
            return path

        return (collect_path(node, []) for node in self.nodes(item))


def conditional_tree(paths):
    tree = FP_Tree()
    condition = None
    for path in paths:
        if condition is None:
            condition = path[-1].item
        point = tree.root
        for node in path:
            next_node = point.search(node.item)
            if not next_node:
                count = node.count if node.item == condition else 0
                next_node = FP_Node(tree, node.item, count)
                point.add(next_node)
                tree.update_route(next_node)
            point = next_node

    for path in tree.prefix_paths(condition):
        count = path[-1].count
        for i in reversed(path[:-1]):
            i.count += count
    return tree


def construct_master_FP_Tree(transactions, minSupport):
    atom_frequence = defaultdict(int)
    for items in transactions:
        for i in items:
            atom_frequence[i] += 1
    support_items = dict((atom, frequence) for atom, frequence in atom_frequence.items() if frequence >= minSupport)

    def support_filter(transaction):
        # descending sort by frequence
        transaction = list(filter(lambda v: v in support_items, transaction))
        transaction.sort(key=lambda v: support_items[v], reverse=True)
        return transaction

    master = FP_Tree()
    for i in map(support_filter, transactions):
        master.add(i)
    return master


def mining_frequent(transactions, minSupport):
    tree = construct_master_FP_Tree(transactions, minSupport)

    def find_with_suffix(tree, suffix):
        for item, nodes in tree.items():
            support = sum(i.count for i in nodes)
            if support >= minSupport and item not in suffix:
                found = [item] + suffix
                yield (found, support)
                cond_tree = conditional_tree(tree.prefix_paths(item))
                for s in find_with_suffix(cond_tree, found):
                    yield s

    for i in find_with_suffix(tree, []):
        yield i


def fp_growth(transactions, minSupport):
    result = []
    for item, support in mining_frequent(transactions, minSupport):
        result.append((item, support))
    result.sort(key=lambda x: x[1],reverse=True)
    return result