# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:58:23 2024

@author: hoang
"""
import random
def question_7(n: int) -> (float, float):
    danhsach= [random.random() for _ in range(n)]
    solonnhat= max(danhsach)
    sonhonhat= min(danhsach)
    return solonnhat, sonhonhat
if __name__=="__main__":
    print(question_7(5))