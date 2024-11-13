# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:40:53 2024

@author: hoang
"""
def question_27(strs: list[str]) -> str:
    if not strs:
        return ""
    strs.sort()
    first_str= strs[0]
    last_str= strs[-1]
    i = 0
    while i < len(first_str) and i < len(last_str) and first_str[i] == last_str[i]:
        i += 1
    return first_str[:i]
if __name__=="__main__":
    print(question_27(["flower", "flow", "flight"]))
    print(question_27(["dog", "racecar", "car"]))
    print(question_27([""]))
    
