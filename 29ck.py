# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:55:17 2024

@author: hoang
"""
def question_29(nums: list) -> float:
    nums.sort()
    n = len(nums)
    if n % 2 != 0:
        return float(nums[n // 2])
    else:
        mid1= nums[(n // 2) -1]
        mid2= nums[(n // 2)]
        return (mid1 + mid2) / 2.0
if __name__=="__main__":
    print(question_29([3, 1, 4, 1, 5]))
    print(question_29([10, 20, 30, 40]))
    
