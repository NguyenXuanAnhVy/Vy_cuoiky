# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:35:07 2024

@author: hoang
"""
def question_16(*arg) -> float:
    # Kiểm tra nếu không có tham số nào được truyền vào
    if len(arg) == 0:
        return 0.0
    # Tính tổng các tham số và chia cho số lượng tham số
    tong= sum(arg)
    soluong= len(arg)
    trungbinhcong = tong / soluong
    return trungbinhcong
if __name__=="__main__":
    print(question_16(4, 4, 6, 12))
    
