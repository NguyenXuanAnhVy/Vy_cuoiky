# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 13:55:58 2024

@author: hoang
"""
def question_22(nums: list[int]) -> None:
    phantukhongzero= [num for num in nums if num != 0]
    soluongzero= len(nums) - len(phantukhongzero)
    nums[:] = phantukhongzero + [0] * soluongzero
if __name__=="__main__":
    print(question_22([0, 1, 0, 3, 12]))
    
