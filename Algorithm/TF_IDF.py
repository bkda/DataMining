# coding=UTF-8
'''
    Created by Tracy on 2016/5/10
    Mail tracyliubai@gmail.com
'''
from math import log

from Algorithm.utils import WordFilter

LOG_BASE = 2.718281828459045

CORPUS_FILE = '../dictionary/corpus'        #Chinese corpus
CORPUS_FILE2 = '../dictionary/corpus2'      #English corpus

class tf_idf:
    def __init__(self):
        with open(CORPUS_FILE, 'r', encoding='utf-8') as f:
            corpus_ZH = f.read().split('\n')
        self.corpus_ZH = corpus_ZH

        with open(CORPUS_FILE2, 'r', encoding='utf-8') as f:
            corpus_EN = f.read().split('\n')
        self.corpus_EN = corpus_EN

    def tf(self, term, doc_list):
        '''
        :param term: word
        :param doc_list: list -> ['My','name','is','tracy']
        :return:TF value
        '''
        return doc_list.count(term.lower()) / float(len(doc_list))

    def idf(self, term, LANG='zh'):
        '''
        :param term: word
        :param corpus:word list
        :param LANG: zh for Chinese & en for English
        :return:IDF value
        '''
        if LANG == 'en':
            corpus = self.corpus_EN
            num = len([True for text in corpus if term.lower() in text.lower().split()])
        else:
            corpus = self.corpus_ZH
            num = len([True for text in corpus if text.find(term) > -1])

        try:
            return 1.0 + log(float(len(corpus) / num), LOG_BASE)
        except ZeroDivisionError:
            return 1.0

    def tf_idf(self, term, doc_list=None, lang='zh'):
        '''
        :param   term: list or a string
        :param   doc_list: if doc_list is None,and term is a word list,it will calculate all of words automatically.
        :param   lang: default Chinese you can choose 'en',it will check lang and choose corpus.
        :return: dict:  {word->TF-IDF}
        '''
        d = {}
        if doc_list == None:
            doc_list = WordFilter(
                term[:])  # remove stopwords and symbols then calculate TF-IDF value of the rest of words
            for i in doc_list:
                d[i] = self.tf(i, term) * self.idf(i, LANG=lang)
            return d
        else:
            if isinstance(term, list):
                for i in term:
                    d[i] = self.tf(i, doc_list) * self.idf(i, LANG=lang)
                return d
            elif isinstance(term, str):
                d[term] = self.tf(term, doc_list) * self.idf(term, LANG=lang)
                return d


sp = tf_idf()
TF_IDF = sp.tf_idf
