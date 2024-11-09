# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:48:03 2024

@author: hoang
"""
def question_6(n: int) -> int:
    #Khởi tạo biến để chứa giai 
    giaithua = 1 
    #Tính giai thừa bằng cách nhân dần các số từ 1 đến n
    for i in range (1, n+1):
         giaithua *= i
    return giaithua  
if __name__=="__main__":
    print(question_6(5))
