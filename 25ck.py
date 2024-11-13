# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 14:25:51 2024

@author: hoang
"""
def question_25(nums: list[int]) -> list[int]:
    binhphuong_nums= [x**2 for x in nums]
    binhphuong_nums.sort()
    return binhphuong_nums
if __name__=="__main__":
    print(question_25([-4, -1, 0, 3, 10]))
    
