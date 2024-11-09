# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 20:50:04 2024

@author: hoang
"""
import math
def question_1(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True


if __name__=="__main__":
    print(question_1(2))
    