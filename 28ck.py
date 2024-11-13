# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:49:22 2024

@author: hoang
"""
from typing import Dict
def question_28(s: str) -> Dict[str, int]:
    count_dict = {}
    for kytu in s: #kytu = char
       if kytu in count_dict:
           count_dict[kytu] += 1
       else: 
           count_dict[kytu] = 1
    return count_dict
if __name__=="__main__":
    print(question_28("Hello world"))
    
           
           
    
    
