# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:58:04 2024

@author: hoang
"""
def question_35(s: str) -> str:
    n = len(s)
    chuoicondainhat= ""
    for dodai in range(1, n // 2 + 1):
        for i in range(n - dodai + 1):
            chuoicon= s[i:i + dodai]
            solanxuathien= s.count(chuoicon)
            if solanxuathien >= 2 and chuoicon not in chuoicondainhat:
                if dodai > len(chuoicondainhat):
                    chuoicondainhat = chuoicon
    return chuoicondainhat
if __name__=="__main__":
    print(question_35("aabcdeaabcd"))
    
