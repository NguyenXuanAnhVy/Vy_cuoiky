# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:08:50 2024

@author: hoang
"""
def question_8() -> str:
    chuoi = input("Nhập chuỗi:")
    #Đảo ngược chuỗi
    chuoidaonguoc= chuoi[:: -1]
    return chuoidaonguoc
if __name__=="__main__":
    ketqua= question_8()
    print("Chuỗi đảo ngược:", ketqua)
    
    
