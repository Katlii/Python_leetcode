# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
     def insert(self, val):
        end =ListNode (val)
        n=self
        while n.next:
            n=n.next
        n.next=end
        
class Solution(object):
    def sortList(self, head):
        if not head:
              return head
        curr=head
        A=[]
        while curr:
            A.append(curr.val)
            curr=curr.next
        A.sort()
        Head=ListNode(A[0])
        for i in range(1, len(A)):
             Head.insert(A[i])

        return Head
             
        
        

head=ListNode(-1)
head.next=ListNode(5)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(0)
out=Solution().sortList(head)
print(out)

