# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:41:12 2024

@author: hoang
"""
def question_33(nums: list[int]) -> tuple[int, int]:
    if len(nums) < 5:
        return None
    dsgiamdan= sorted(nums, reverse=True)
    dstangdan= sorted(nums)
    phantulonthu2= dsgiamdan[1]
    phantunhothu5= dstangdan[4]
    return (phantulonthu2, phantunhothu5)
if __name__=="__main__":
    print(question_33([10, 20, 4, 45, 99, 3, 17, 8, 1]))
#Với danh sách nums = [10, 20, 4, 45, 99, 3, 17, 8, 1], sau khi sắp xếp:
#Sắp xếp giảm dần: [99, 45, 20, 17, 10, 8, 4, 3, 1] → Phần tử lớn thứ 2 là 45.
#Sắp xếp tăng dần: [1, 3, 4, 8, 10, 17, 20, 45, 99] → Phần tử nhỏ thứ 5 là 10.    