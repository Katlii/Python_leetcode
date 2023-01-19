import copy
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def oddEvenList(self, head):
        curr=head
        a=copy.deepcopy(head)
        while curr.next:
            tmp=curr.next.next
            curr.next=curr.next.next
            curr=curr.next
        while a.next:
            curr.next=a.next
            curr=a.next
            a=a.next.next
        return head.next.next.next.next.next.next.next.val
        




head=ListNode(2)
head.next=ListNode(1)
head.next.next=ListNode(3)
head.next.next.next=ListNode(5)
head.next.next.next.next=ListNode(6)
head.next.next.next.next.next=ListNode(4)
head.next.next.next.next.next.next=ListNode(7)
out=Solution().oddEvenList(head)
print(out)
