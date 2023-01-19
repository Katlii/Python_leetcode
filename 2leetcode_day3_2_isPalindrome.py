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
        if A==B: return True
        else: False


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(2)
head.next.next.next=ListNode(1)
out=Solution().isPalindrome(head)
print(out)
