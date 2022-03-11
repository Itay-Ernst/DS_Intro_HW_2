# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 17:26:06 2022

@author: iernst
"""
def reverse(sentence, reverse_word):
    try:
        if type(reverse_word) is not str:
            return ("invalid input")
        if reverse_word not in sentence:
            return ("The word was not found")
        else:
            revers=reverse_word[::-1]
            New_sent = sentence.replace(reverse_word,revers,1)
            return (New_sent)
    except:
        return ("input error detected")
    