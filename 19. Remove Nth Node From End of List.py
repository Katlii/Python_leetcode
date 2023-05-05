#Given the head of a linked list, remove the nth node from
#the end of the list and return its head.

#Input: head = [1,2,3,4,5], n = 2
#Output: [1,2,3,5]


class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n: int) :
        size=0
        point=head
        while point:
            size+=1
            point=point.next
        if n==size:
            return head.next
        delPos=size-n+1
        point=head
        while delPos!=2:
            point=point.next
            delPos-=1
        if point.next.next: point.next=point.next.next
        else: point.next=None
        return head
            
        



head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

print(Solution().removeNthFromEnd(head, 5))
