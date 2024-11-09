# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 00:02:36 2024

@author: hoang
"""
from typing import Optional
def question_20() -> Optional[str]:
    giatri= input("Nhập:")
    if giatri == "":
        return None 
    return giatri
if __name__=="__main__":
    ket_qua = question_20()
    print(ket_qua)
