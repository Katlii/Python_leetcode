class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def contains(self, val):
    
        curr=self.head
        while curr:
            if curr.val==val:
                return True
            else: curr=curr.next
        return False

    def add(self, val):
        if self.head is None:
            Head=Node(val)
            self.head=Head
        else:
            Head=Node(val)
            curr=self.head
            while  curr.next:
                curr=curr.next
            curr.next=Head
            

    def get(self, index):
        last=self.head
        indexX=0
        while indexX!=index:
            indexX+=1
            last=last.next
        return last.val
        

    def remove(self, val):
        last=self.head
        curr=last.next
        if last.val==val:
            self.head=last.next
        else:
            while curr.val!=val:
                curr=curr.next
                last=last.next
            last.next=curr.next
        return last.val
        

myLL= LinkedList()
print(myLL.add(1))
print(myLL.add(43))
print(myLL.add(45))
print(myLL.get(2))              #return 45
print(myLL.remove(43))    #now the linked list is 1->45
print(myLL.contains(1))
print(myLL.get(0))        #return 1
print(myLL.add(10))        #1->45->10
print(myLL.add(100))      #1->45->10->100
print(myLL.contains(10))   #True
print(myLL.contains(45))    #True
print(myLL.get(2))         #10
print(myLL.remove(1))    #45->10->100
print(myLL.get(2))        #100
