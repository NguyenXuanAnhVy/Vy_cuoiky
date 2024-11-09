# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:10:01 2024

@author: hoang
"""
import random
def question_2(n: int) -> (int, float):
    songaunhien = []
    for _ in range(n):
        songaunhien.append(random.randint(1, 100))
    tong= sum(songaunhien)
    trungbinh= tong / n
    return tong, trungbinh

if __name__=="__main__":
    print(question_2(12))
