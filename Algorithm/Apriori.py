# coding=UTF-8
'''
    Created by Tracy on 2016/5/29
    Mail tracyliubai@gmail.com
'''
from collections import defaultdict
from itertools import combinations
from Algorithm.utils import isSubList


def generate_atom_frequence(data_sets):
    item_freq = defaultdict(int)
    for sub_list in data_sets:
        for i in sub_list:
            item_freq[i] = 1 if i not in item_freq.keys() else item_freq[i] + 1
    return item_freq


def returnConditional(num, data_sets=None):
    def subset(condition):
        for i in range(len(condition)):
            samp = list(condition[:])
            del samp[i]
            if tuple(samp) not in data_sets:
                return False
        return True

    if num == 2:
        return [i for i in combinations(data_sets, num)]
    else:
        freq = support_filter(generate_atom_frequence([list(i) for i in data_sets]), support=num - 1)
        if len(freq) < num:
            return []
        else:
            return [i for i in combinations(freq.keys(), num) if subset(i)]


def generate_frequence_dict(match_list, conditional, cond_dict=defaultdict(lambda: 0)):
    for i in conditional:
        for j in match_list:
            if isSubList(j, list(i)):
                cond_dict[i] += 1
    return cond_dict


def support_filter(transac, support):
    return {k: v for k, v in transac.items() if v >= support}


def apriori(transactions, minSupport):
    freq_sets = support_filter(generate_atom_frequence(transactions), support=minSupport)
    k = 2
    while True:
        condition = returnConditional(num=k, data_sets=freq_sets)
        freq_sets = support_filter(generate_frequence_dict(transactions, condition), support=minSupport)
        k += 1
        if freq_sets == {} or condition == []:
            break
    for k, v in freq_sets.items():
        print(k, v)