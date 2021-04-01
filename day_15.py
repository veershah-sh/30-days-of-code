class Node:
   def __init__(self,data):
      self.data = data
      self.next = None 
class Solution: 
   def display(self,head):
      current = head
      while current:
         print(current.data,end='---> ')
         current = current.next

   def insert_at_last(self,head,data): 
      nodeData = Node(data)
      if head is None:
         head = nodeData
      else:
         current = head
         while current.next:
            current = current.next
         current.next = nodeData
      return head
      
mylist= Solution()
T=int(input())
head=None
for i in range(T):
   data=int(input())
   head=mylist.insert_at_last(head,data)    
mylist.display(head); 