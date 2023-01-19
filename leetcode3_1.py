# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0):
         self.val = val
         self.next = None
class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

list1=ListNode(1)
list1.next=ListNode(2)
list1.next.next=ListNode(4)
list2=ListNode(3)
list2.next=ListNode(5)
list2.next.next=ListNode(6)

out=Solution().mergeTwoLists(list1, list2)
print(out)
