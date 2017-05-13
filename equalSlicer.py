# -*- coding: utf-8 -*-
"""
Created on Wed May 03 20:57:43 2017

@author: Owner
"""
a = 'a'*198 + 'b'
b = 'abcd'*3
c = 'a'*199
s = 'abcabcabcabc' 
def answer(s):
    # If all the elements of the string are the same.
    if s[1:] == s[0]*len(s[1:]):
        return int(len(s))
    # If the number of unique colors is even
    elif len(s) % 2 == 0:
        i = 2 #Cut after the ith color
        while i <= len(s) / 2:
            l = len(s) - len(s[:i]) # length of sequence after cut 
            k = l / len(s[:i])
            #If i = half the length of the sequence
            if i == (len(s) / 2) & (s[:i] == s[i:]):
                return len(s) / i
                break
            #Checks if cut sequence is being repeated
            elif s[:i]*k == s[i:]:
                return len(s) / len(s[:i])
            else:
                i+=1
        return 1
    #No equal slices can be cut.
    else:
        return 1
            
            
            

answer(s)