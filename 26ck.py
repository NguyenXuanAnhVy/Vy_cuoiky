# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:30:49 2024

@author: hoang
"""
import collections
def question_26(s: str) -> int:
    char_count= collections.Counter(s)
    length = 0
    for count in char_count.values():
        length += count // 2 * 2
        if count % 2 == 1:
            length += 1
    return length
if __name__=="__main__":
    print(question_26("abccccdd")) 
    print(question_26("a"))          
    print(question_26("bb")) 
        
        