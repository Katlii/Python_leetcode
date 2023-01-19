class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def contains(self, val):
        last=self.head
        while last:
            if val==last.val:
                return True
            else: last=last.next
        return False
    def add(self, val):
        Head=Node(val)
        if self.head is None:
            self.head=Head
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=Head

    def get(self, index):
        last=self.head
        index_in_LL=0
        while index_in_LL <=index:
            if index_in_LL==index:
                return last.val
            last=last.next
            index_in_LL+=1

    def remove(self, val):
        last=self.head
        if last.val==val:
            self.head=last.next
        else:
            last=last.next
            while last.val!=val:
                self.head=last
                last=last.next
            self.head.next=last.next
            return self.head.next.val

myLL= LinkedList()
print(myLL.add(1))
print(myLL.add(43))
print(myLL.add(45))
print(myLL.get(2))              #return 5
print(myLL.remove(1))    #now the linked list is 1->3
print(myLL.contains(1))
print(myLL.get(0))

