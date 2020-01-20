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
    
    def remove(self,item):
        pass

    def search(self,item):
        pass

    def isEmpty(self):

        if self.head == None:
            return True

        else:
            return False

    def size(self):
        
        return self.sizeList

    def append(self,item):
        pass

    def index(self,item):
        pass

    def insert(self,pos,item):
        pass

    def pop(self):

        if self.head == None:
            return None

        if self.head.next == None:
            self.head = None
            return None

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    # def pop(self,pos):
    #     pass

    def insertFirst(self,ele):
        
        node = Node(ele)
        node.next = self.head
        self.head = node

    def dispalyList(self):
        
        current = self.head
        
        while current:
            print(current.data," <---- ",end="")
            current = current.next
        
        print("None")
