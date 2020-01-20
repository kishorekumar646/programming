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
        
        current = self.head
        
        if current == None:
            return None
        
        else:
            while current:
                if current.data == item:
                    return True

                current = current.next
            
            return False

    def isEmpty(self):

        if self.head == None:
            return True

        else:
            return False

    def size(self):
        
        return self.sizeList

    def append(self,item):
        
        node = Node(item)
        
        if self.head is None:
            self.head = node
            self.sizeList += 1
        
        else:
            last = self.head
           
            while last.next:
                last = last.next
           
            last.next = node
            self.sizeList += 1

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

    def delete(self,key):
        
        current = self.head

        if current is not None:
            if current.data == key:
                self.head = current.next
                current = None
                return

        while current:
            if current.data == key:
                break
            prev = current
            current = current.next

        prev.next = current.next
        # current = None

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

class Stack:

    def __init__(self):

        self.stack_list = []
        self.top = 0

    def push(self,item):
        
        self.stack_list.append(item)
        self.top += 1

    def pop(self):
        if self.stack_list == None:
            return None
        else:
            last_element = self.stack_list[self.top]
            self.top -= 1
            return last_element

    def peek(self):
        pass

    def isEmpty(self):
        pass

    def size(self):
        pass