#!/usr/bin/env python3

def return_evens(num_list):
    evens_list = []
    for n in num_list:
        if n % 2 == 0:
            evens_list.append(n)
    return(evens_list)

def make_exclamation(sentence_list):
    exclamations = []
    for s in sentence_list:
        exclamations.append(f'{s}!')
    return exclamations