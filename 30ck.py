# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:08:44 2024

@author: hoang
"""
from typing import Dict
def question_30(paragraph: str) -> Dict[str, int]:
    words = paragraph.lower().split()
    word_count= {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count
if __name__=="__main__":
    print(question_30("Hello world! Hello everyone. Welcome to the world of Python."))
    
