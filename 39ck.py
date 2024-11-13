# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:40:35 2024

@author: hoang
"""
def question_39(prices: list[int]) -> int:
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        profit = price - min_price
        max_profit= max(max_profit, profit)
        min_price= min(min_price, price)
    return max_profit
if __name__=="__main__":
    print(question_39([7, 1, 5, 3, 6, 4]))
    
        
        
