# -*- coding: utf-8 -*-
"""
Created on Fri May 05 16:20:24 2017

@author: Owner
"""
s = '---><<--'
def answer(s):
    salutes = 0
    if '>' and '<' not in s:
        return 0
    for i in range(len(s)):
        if s[i] == '<':
            for e in s[:i]:
                if e == '>':
                    salutes+=1
        elif s[i] == '>':
            for e in s[i:]:
                if e == '<':
                    salutes+=1
        else:
            continue
    return salutes
        
print("Salutes: " + str(answer(s)))