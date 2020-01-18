class Node:
    
    def __init__(self,data):
        
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        
        self.head = None
        self.sizeList = 0

    def add(self,item):

        node = Node(item)
        
        if self.head is None:
            self.head = node
            self.sizeList += 1
        
        else:
            last = self.head
           
            while last.next:
                last = last.next
                self.sizeList += 1
           
            last.next = node
    
    def insertFirst(self,ele):
        
        node = Node(ele)
        node.next = self.head
        self.head = node

    def size(self):
        
        return self.sizeList

    def dispalyList(self):
        
        current = self.head
        
        while current:
            print(current.data," ----> ",end="")
            current = current.next
        
        print("None")
