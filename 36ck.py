# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:08:34 2024

@author: hoang
"""
def question_36(nums: list[int]) -> list[list[int]]:
    kq = []
    def backtrack(start: int):
        if start == len(nums):
            kq.append(nums[:])
            return
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start]
    backtrack(0)
    return kq
if __name__=="__main__":
    print(question_36([1, 2, 3]))
    
