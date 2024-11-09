# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:46:12 2024

@author: hoang
"""
import random
def question_17(n: int) -> list:
    ds= [random.randint(1, 100) for _ in range(n)]
    ds.sort(reverse= True)
    return ds
if __name__=="__main__":
    print(question_17(2))
