# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0):
         self.val = val
         self.next = None
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        self.size=0
        start, end=head, head
        while start:
            self.size+=1
            start=start.next
        index=self.size-n
        i=1
        if index==0:
            return head.next
        while i!=index:
            end=end.next
            i+=1
        if end.next.next:
            end.next=end.next.next
        else:
            end.next=None
        return head.val


head=ListNode(1)
head.next=ListNode(2)
#head.next.next=ListNode(3)
#head.next.next.next=ListNode(4)
#head.next.next.next.next=ListNode(5)
out=Solution().removeNthFromEnd(head, 1)
print(out)



