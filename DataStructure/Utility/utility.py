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
            element = self.head.data
            self.head = None
            return element

        current = self.head
        while current.next.next:
            current = current.next

        element = (current.next).data
        current.next = None
        
        return element

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
        self.top = -1

    def push(self,item):
        self.top += 1
        self.stack_list.append(item)
        return

    def pop(self):
        if self.top == -1:
            return None
        else:
            last_element = self.stack_list[self.top]
            self.stack_list.pop()
            self.top -= 1
            return last_element

    def peek(self):
        
        if self.top == -1:
            return None
        
        else:
            return self.stack_list[self.top]

    def isEmpty(self):
        
        if self.top == -1:
            return True
        
        else:
            return False


    def size(self):
        
        return self.top

    def dispaly_stack_list(self):

        print("Stack : ",end="")
        if self.top == -1:
            print("Empty")
            return
        
        for numbers in range(self.top+1):
            print(self.stack_list[numbers],end=" ")
        print()
        
class Queue:

    def __init__(self):
        self.queue_list = []
        self.front = 0
        self.rear = -1

    def enqueue(self,item):
        self.queue_list.append(item)
        self.rear +=1

    def dequeue(self):
        if self.rear == -1:
            print("queue list is underflow")
        else:
            element = self.queue_list[self.front]
            self.queue_list.pop(0)
            self.rear -=1
            return element

    def isEmpty(self):
        
        if self.queue_list == []:
            return True
        
        else:
            return False

    def size(self):
        
        return self.rear + 1

    def dispaly_queue_list(self):
        print("Queue : ",end="")
        if self.rear == -1:
            print("Empty")
            return
        
        for numbers in range(self.rear+1):
            print(self.queue_list[numbers],end=" ")
        print()

class Dequeue:

    def __init__(self):
        self.dequeue_list = []

    def addFront(self,item):

        self.dequeue_list.append(item)

    def addRear(self,item):

        self.dequeue_list.insert(0,item)

    def removeFront(self):
        
        self.dequeue_list.pop()

    def removeRear(self):

        self.dequeue_list.pop(0)

    def isEmpty(self):
        
        if self.dequeue_list == []:
            return True

        else:
            return False

    def size(self):
        
        return len(self.dequeue_list) + 1

    def dispaly_dequeue_list(self):

        print("Deque : ",end="")
        for number in range(len(self.dequeue_list)):
            print(self.dequeue_list[number],end=" ")
        print()