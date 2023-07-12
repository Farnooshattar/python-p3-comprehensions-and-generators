#!/usr/bin/env python3

num_list = [0, 1, 3, 5, 7, 8, 9]
def return_evens(num_list):
    return [n for n in num_list if n%2 == 0 ]

sentence_list = ["Hello", "I'm doing great", "Python is fun"]

def make_exclamation(sentence_list):
     return [n+"!" for n in sentence_list ]