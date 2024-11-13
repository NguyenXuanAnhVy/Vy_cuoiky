# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:16:50 2024

@author: hoang
"""
def question_37(s: str) -> bool:
    ds= []
    capngoac= {')':'(', '}':'{', ']':'['}
    for kytu in s:
        if kytu in "({[":
            ds.append(kytu)
        elif kytu in ")}]":
            if ds and ds[-1] == capngoac[kytu]:
                ds.pop() # Loại bỏ dấu ngoặc mở tương ứng
            else: 
                return False
    return len(ds) == 0
if __name__=="__main__":
    print(question_37("()"))  
    print(question_37("()[]{}")) 
    print(question_37("(]"))  
    print(question_37("([)]"))  
    print(question_37("{[]}"))
