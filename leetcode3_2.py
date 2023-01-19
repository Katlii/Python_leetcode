# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def reverseList(self, head):
        A=[]
        Head= LinkedList=ListNode()
        last=Head
        curr=head
        while curr:
            A.append(curr.val)
            curr=curr.next
        A.reverse()
        for i in A:
            Head=ListNode(i)
            while last.next:
                last=last.next
            last.next=Head
        return LinkedList.next





head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)

out=Solution().reverseList(head)
print(out)
