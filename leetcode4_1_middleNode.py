# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def middleNode(self, Head):
        size=0
        self.head=Head
        curr=Head
        while curr is not None:
            size+=1
            curr=curr.next
        if size%2==0:
            index=size//2+1
        else:
            index=size//2+1
        f=Solution().find_index(Head, index)
        return f

    def find_index(self, Head, index):
        last=self.head=Head
        curr=0
        while curr!=index:
            curr+=1
            last=last.next
        return last
        




head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

out=Solution().middleNode(head)
print(out)

