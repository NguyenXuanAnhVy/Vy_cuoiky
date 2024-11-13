# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:10:48 2024

@author: hoang
"""
def question_24(nums: list[int]) -> int:
    count= {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    n = len(nums) // 2
    for num, cnt in count.items():
        if cnt > n:
            return num
if __name__=="__main__":
    print(question_24([3, 2, 3]))  
    print(question_24([2, 2, 1, 1, 1, 2, 2]))