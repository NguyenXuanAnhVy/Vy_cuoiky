# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 22:22:21 2024

@author: hoang
"""
import re 
def question_9(s: str) -> bool:
    # Bước 1: Chuyển tất cả các ký tự viết hoa thành viết thường và loại bỏ ký tự không phải chữ cái hoặc số
    s = s.lower() #Chuyển tất cả các ký tự thnahf chữ thường
    s = re.sub(r'[^a-z0-9]', '', s) # Loại bỏ các ký tự không phải chữ cái hoặc số
    # Bước 2: Kiểm tra xem chuỗi có đọc giống nhau từ trái sang phải và từ phải sang trái không
    return s == s[::-1] 
if __name__=="__main__":
    print(question_9("A man, a plan, a canal, Panama"))
