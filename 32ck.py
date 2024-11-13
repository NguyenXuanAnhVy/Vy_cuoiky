# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:32:07 2024

@author: hoang
"""
from typing import List, Tuple
def question_32(nums: List[int]) -> Tuple[List[int], List[int]]:
    sochan= [x for x in nums if x % 2 == 0]
    sole= [x for x in nums if x % 2 !=0 ]
    sochan.sort(reverse=True)
    sole.sort()
    return (sochan, sole)
if __name__=="__main__":
    print(question_32([4, 1, 3, 2, 7, 8, 5]))
    
    
    
