# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:37:37 2024

@author: hoang
"""
from typing import Optional 
def question_21(nums: list[int], target: int) -> Optional[tuple[int, int]]:
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return (nums[i], nums[j])
    return None
if __name__=="__main__":
    print(question_21([2, 5, 8, 9], 10))
    
