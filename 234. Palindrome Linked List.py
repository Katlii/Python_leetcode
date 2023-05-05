#Given the head of a singly linked list, return true if it is a 
#palindrome or false otherwise.

#Input: head = [1,2,2,1]
#Output: true


import copy
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
         A, B=[], []
         start=head
         while start:
             A.append(start.val)
             start=start.next
         B=copy.deepcopy(A)
         A.reverse()
         print(A, B)
         if A==B:
             return True
         else: False
        
"""class Solution:
    def isPalindrome(self, head) -> bool:
         N=0
         a=[]
         point=head
         while point:
              N+=1
              point=point.next
         start=1
         end=N
         point=head
         while start!=N//2+1:
            for i in range(1, end):
                 point=point.next
            if head.val==point.val: a.append(True)
            else: a.append(False)
            head=head.next
            start+=1
            end-=2
            point=head
         if False in a: return False
         else: return True
"""     


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(4)
head.next.next.next=ListNode(1)
out=Solution().isPalindrome(head)
print(out)
