# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break
        if not (fast and fast.next): return None
        while head != slow:
            head, slow = head.next, slow.next
        return head.val

        """
        self.head=Head
        curr=Head
        A=[]
        index=0
        while curr:
            A.append(curr.val)
            curr=curr.next
        lastnode=A[len(A)-1]
        while self.head:
            if self.head.val==lastnode:
                return self.head
            else:
                self.head=self.head.next
        return None
        """



head=ListNode(3)
head.next=ListNode(2)
head.next.next=ListNode(0)
head.next.next.next=ListNode(-4)


out=Solution().detectCycle(head)
print(out)
