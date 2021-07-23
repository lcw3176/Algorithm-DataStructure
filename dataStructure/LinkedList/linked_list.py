class Node:
    def __init__(self):
        self.data = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = Node()
        self.length = 0
    

    def __add_first(self, data):
        first_node = Node()
        first_node.data = data
        first_node.next = self.tail
        
        self.head = first_node
        self.length += 1


    def __add_last(self, data):
        new_tail_node = Node()

        self.tail.data = data
        self.tail.next = new_tail_node
        self.tail = self.tail.next
        
        self.length += 1


    def add(self, data):
        if self.head == None or self.head.data == None:
            self.__add_first(data)
        else:
            self.__add_last(data)
    

    def get(self, index):
        if index >= self.length or self.length == 0:
            raise Exception("인덱스 초과")
        
        node = self.head
        for _ in range(index):
            node = node.next
        
        return node.data


    def remove(self, index):
        if index >= self.length or self.length == 0:
            raise Exception("인덱스 초과")
        
        count = 0
        node = self.head
        prev = None

        while count != index:
            prev = node
            node = node.next
            count += 1
        
        if node == self.head:
            self.head = node.next
        else:
            prev.next = node.next

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
        while node.data != None:
            print(node.data, end=" ")
            node = node.next
        print()