# -*- coding: utf-8 -*-
"""Day16_Exceptions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JP4e00y40NG8OalPkVZVB_rcrG3B7URu
"""

S = input().strip()
try:
  i = int(S)
  print(S)
except:
  print("Bad String")