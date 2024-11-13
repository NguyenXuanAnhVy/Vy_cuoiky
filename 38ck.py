# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:32:44 2024

@author: hoang
"""
def question_38(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a, b = 1, 2
    for i in range(3, n + 1):
        a, b = b, a + b #a là F(i-2), b là F(i-1)
    return b
if __name__=="__main__":
    print(question_38(3))
    
