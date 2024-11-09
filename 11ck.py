# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:55:17 2024

@author: hoang
"""
def question_11(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1: 
        return 1
    else:
        # Khởi tạo hai giá trị F(0) và F(1)
        f0, f1 = 0, 1
        for i in range (2, n+1):
            # Tính F(i) theo công thức F(i) = F(i-1) + F(i-2)
            f0, f1 = f1, f0 + f1
        return f1
if __name__=="__main__":
    print(question_11(17))
    
