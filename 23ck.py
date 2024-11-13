# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:03:36 2024

@author: hoang
"""
def question_23(nums: list[int]) -> bool:
    return len(nums) != len(set(nums))
if __name__=="__main__":
    print(question_23([1, 2, 3, 4]))
    print(question_23([1, 2, 2, 4]))
