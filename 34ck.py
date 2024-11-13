# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:48:58 2024

@author: hoang
"""
def question_34(s: str) -> int:
    # Tạo một bộ nhớ để theo dõi các ký tự trong cửa sổ
    char_set = set()
    start = 0
    max_length = 0
    for end in range(len(s)):
        # Nếu ký tự đã có trong cửa sổ, di chuyển start để loại bỏ ký tự bị lặp lại
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1
        char_set.add(s[end])
        max_length = max(max_length, end - start + 1)
    return max_length
if __name__=="__main__":
   print(question_34("abcabcbb")) 
   print(question_34("bbbbb"))     
   print(question_34("pwwkew"))