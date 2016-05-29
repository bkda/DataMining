# coding=UTF-8
'''
    Created by Tracy on 2016/5/21
    Mail tracyliubai@gmail.com
'''
from Algorithm.Viterbi import viterbi
states = ('Healthy', 'Fever')
start_probability = {'Healthy': 0.6, 'Fever': 0.4}
transition_probability = {
    'Healthy': {'Healthy': 0.7, 'Fever': 0.3},
    'Fever': {'Healthy': 0.4, 'Fever': 0.6},
}
observations = ('normal', 'cold', 'dizzy')
emission_probability = {
    'Healthy': {'normal': 0.5, 'cold': 0.4, 'dizzy': 0.1},
    'Fever': {'normal': 0.1, 'cold': 0.3, 'dizzy': 0.6},
}
print(viterbi(observations, states, start_probability, transition_probability, emission_probability))
