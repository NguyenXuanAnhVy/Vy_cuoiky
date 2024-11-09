# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:40:17 2024

@author: hoang
"""
def question_5(lst: list, x: int) -> int or None:
    for i in range(len(lst)):
        # Kiểm tra xem phần tử tại vị trí i có bằng x không
        if lst[i] == x:
            return i #nếu tìm thấy, trả về vị trí
    return None 
lst = [1, 2, 3, 4, 5]
x = 3 
if __name__=="__main__":
    print(question_5(lst, x))
    
