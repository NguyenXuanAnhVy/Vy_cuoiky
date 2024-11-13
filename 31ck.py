# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:19:45 2024

@author: hoang
"""
from typing import List
def question_31(paragraph: str, n: int) -> List[str]:
    paragraph = paragraph.lower()
    words = paragraph.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    total_words = len(words)
    result = []
    for word, count in word_count.items():
        if count / total_words > 0.2:
            result.append(word)
    return result
paragraph =  "apple apple banana orange orange apple"
n = 2
print(question_31(paragraph, n))

