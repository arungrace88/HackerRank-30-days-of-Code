# -*- coding: utf-8 -*-
"""Day15_LinkedList.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RyWOTJbdCrCaMhZE2Q_VkSHfaLqgW9vD
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data): 
    #Complete this method
        new = Node(data)
        if not head:
            return new
        current = head
        while current.next:
            current = current.next
    
        current.next = new
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head);