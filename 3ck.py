# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 21:24:28 2024

@author: hoang
"""
def question_3(n: str) -> (int, int):
    #Khởi tạo biến đếm số ký tự viết hoa và viết thường:
    viethoa= 0
    vietthuong= 0
    #Duyệt qua từng ký tự trong chuỗi
    for kytu in n:
        if kytu.isupper(): #Ktr nếu ký tự là viết hoa
            viethoa +=1
        if kytu.islower(): #Ktr nếu ký tụ là viết 
            vietthuong +=1
    #Trả về kết quả dưới dạng tuple
    return (viethoa, vietthuong)

if __name__=="__main__":
    print(question_3("Hello World"))
            
