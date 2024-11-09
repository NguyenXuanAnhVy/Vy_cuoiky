# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:00:34 2024

@author: hoang
"""
import random
#Hàm ktra
def kiemtranguyento(n: int) -> bool:
    if n<=1:
        return False
    for i in range(2, int(n** 0.5) + 1):
        if n % i == 0:
            return False
    return True
#Hàm chính 
def question_12() -> bool:
     songaunhien= random.randint(1, 1000)
     return kiemtranguyento(songaunhien)
if __name__=="__main__":
    print(question_12()) 
     
