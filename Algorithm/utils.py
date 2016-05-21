# coding=UTF-8
'''
    Created by Tracy on 2016/5/11
    Mail tracyliubai@gmail.com
'''
DICT = "../dictionary/stopword"
stopword = []


def WordFilter(word, CUSTOM_STOPWORD=[]):
    '''
    :param word: list or stopword,remove stopword and special symbol.
    :param CUSTOM_STOPWORD: custom stopword  TYPE -list
    :return: Filter result
    '''
    load_dict()
    stopword.extend(CUSTOM_STOPWORD)
    if isinstance(word, list):
        temp = word[:]
        for i in temp:
            if not i.isalpha() or i in stopword:
                word.remove(i)
        return word
    elif isinstance(word, dict):
        for i in word.keys():
            if not i.isalpha() or i in stopword:
                word[i] = 0
        return word


def load_dict():
    global stopword
    with open(DICT, 'r') as f:
        stopword = f.read().split('\n')


def isSubList(pattern_list, sub_list):
    pattern, sublist = pattern_list[:], sub_list[:]
    while sublist != []:
        if sublist[-1] in pattern:
            pattern.remove(sublist[-1])
            del sublist[-1]
            if sublist == []:
                return True
        else:
            return False
