#Given the head of a singly linked list, group all the nodes
#with odd indices together followed by the nodes
#with even indices, and return the reordered list.

#Input: head = [1,2,3,4,5]
#Output: [1,3,5,2,4]


import copy
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def oddEvenList(self, head):
        if head is None:
            return head
        currentOdd = head
        count = 2
        node = head
        pre = node
        node = node.next
        while node is not None:
            if count % 2 == 0:
                pre = node
                node = node.next
            else:
                next = node.next
                pre.next = next
                temp = currentOdd.next
                currentOdd.next = node
                node.next = temp
                currentOdd = node
                node = next
            count += 1
        return head

"""class Solution:
    def oddEvenList(self, head):
        pointOdd=head
        pointEven=copy.deepcopy(head.next)
        while pointOdd.next is not None:
             if pointOdd.next is not None:
                  pointOdd.next=pointOdd.next.next
             if pointOdd.next is not None:
                  pointOdd=pointOdd.next
     
                  
        while pointEven is not None:
             if pointEven.next is not None:
                  #print(pointEven.val)
                  pointOdd.next=pointEven
                  pointEven.next=pointEven.next.next
             pointEven=pointEven.next
             pointOdd=pointOdd.next
        
     
        return head.next.next.next.next.next.val
"""        




head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)
head.next.next.next.next.next.next=ListNode(7)
head.next.next.next.next.next.next.next=ListNode(8)
out=Solution().oddEvenList(head)
print(out)
