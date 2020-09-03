# -*- coding: utf-8 -*-
"""Day17_More Exceptions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14EaPv7Rz_UJHIr_4yK_mGEbm2AyftLVj
"""

class Calculator():
    #
    def power(self,num, power): 
        if(num < 0 or power < 0):
            raise Exception("n and p should be non-negative")
        else:
            return pow(num,power)

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)