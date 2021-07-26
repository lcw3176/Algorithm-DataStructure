class Node:
    def __init__(self):
        self.data = None
        self.next = None
        self.before = None

class Deque:
    def __init__(self):
        self.front = Node()
        self.rear = Node()
        self.size = 0

        
    def push_front(self, data):
        if self.size == 0:
            self.front.data = data
            self.front.next = self.rear
            self.rear.before = self.front
        else:  
            node = Node()
            node.data = data
            self.front.before = node
            node.next = self.front
            self.front = node
        self.size += 1


    def pop_front(self):
        value = self.front.data
        self.front = self.front.next
        self.size -= 1
        return value


    def push_back(self, data):
        if self.size == 0:
            self.rear.data = data
            self.rear.before = self.front
            self.front.next = self.rear
        else:
            node = Node()
            node.data = data
            self.rear.next = node
            node.before = self.rear
            self.rear = node
        self.size += 1


    def pop_back(self):
        value = self.rear.data
        self.rear = self.rear.before
        self.size -= 1
        return value


    def empty(self):
        if self.size == 0:
            return True
        return False 


    def __len__(self):
        return self.rear
