# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:12:07 2024

@author: hoang
"""
def question_13(s: str) -> int:
    # Loại bỏ các khoảng trắng dư thừa ở đầu và cuối chuỗi, sau đó tách chuỗi thành danh sách các từ
    danhsachtu= s.strip().split()
    #Đếm số lượng từ trong ds
    return len(danhsachtu)
if __name__=="__main__":
    print(question_13("Nguyễn Xuân Ánh Vy"))
