class Node:
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0
    

    def __add_first(self, data):
        node = Node()
        node.data = data
        node.next = None
        
        self.head = node
        self.length += 1


    def __add_next(self, data, node):
        new_node = Node()
        new_node.data = data

        while node.next != None:
            node = node.next
        
        node.next = new_node
        self.length += 1


    def add(self, data):
        node = self.head

        if node == None:
            self.__add_first(data)
        else:
            self.__add_next(data, node)
    

    def get(self, index):
        if index >= self.length:
            raise Exception("인덱스 초과")
        
        node = self.head
        for _ in range(index):
            node = node.next
        
        return node.data


    def remove(self, index):
        if index >= self.length:
            raise Exception("인덱스 초과")
        
        node = self.head
        prev = None

        for _ in range(index):
            prev = node
            node = node.next            

        for _ in range(index, self.length - 1):
            temp = node.next     
            node.data = temp.data 
            prev = node
            node = node.next
        
        if self.length == 1:
            self.head = None
        else:
            prev.next = None
        
        self.length -= 1


    def contains(self, element):
        node = self.head
        for _ in range(self.length):
            if node.data == element:
                return True
            node = node.next
        
        return False


    def clear(self):
        for _ in range(self.length):
            self.remove(0)


    def size(self):
        return self.length


    def indexOf(self, element):
        node = self.head
        index = 0

        for _ in range(self.length):
            if node.data == element:
                return index
            index += 1
            node = node.next
        
        return -1

    def display(self):
        node = self.head
        
        while node:
            print(node.data, end=" ")
            node = node.next
        print()
