# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:49:20 2024

@author: hoang
"""
def question_10() -> None:
    chuoi = input("Nhập chuỗi: ")
    #Chuyển chuỗi nhập vào thành một danh sách các số nguyên
    songuyen= chuoi.split()
    if not songuyen:
        return None
    #Chuyển các phần tử trong danh sách từ chuỗi sang số nguyên
    songuyen = [int(so) for so in songuyen]
if __name__=="__main__":
    songuyen = question_10()
    print("Danh sách các số nguyên đã nhập:", songuyen)
