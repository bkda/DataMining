# coding=UTF-8
'''
    Created by Tracy on 2016/5/21
    Mail tracyliubai@gmail.com
'''


def viterbi(observ, states, start_prob, trans_prob, emit_prob):
    '''
    :param obs:         observations set tuple
    :param states:      states tuple
    :param start_prob:  start probability stopword
    :param trans_prob:  transition probability -> nested stopword
    :param emit_prob:   emission probability -> nested stopword
    :return:            probability  &   path
    '''
    V = [{}]
    path = {}
    for i in states:
        V[0][i] = start_prob[i] * emit_prob[i][observ[0]]
        path[i] = [i]
    for i in range(1, len(observ)):
        V.append({})
        newpath = {}
        for j in states:
            (prob, state) = max([(V[i - 1][k] * trans_prob[k][j] * emit_prob[j][observ[i]], k) for k in states])
            V[i][j] = prob
            newpath[j] = path[state] + [j]
        path = newpath
    printNicely(V)
    (prob, state) = max([(V[len(observ) - 1][y], y) for y in states])
    return (prob, path[state])


def printNicely(v):
    for i in range(0, len(v) + 1): print('{:^7}'.format(i), end='')
    for i in v[0].keys():
        print()
        d = [round(v[j][i], 7) for j in range(len(v))]
        d.insert(0, i)
        for j in d: print('{:^7}'.format(j), end='')
    print('\n')
