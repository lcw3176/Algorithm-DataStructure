from cArray import Array


class ArrayList:
    def __init__(self):
        self.size = 10
        self.index = 0
        self.arr = Array(self.size)

    def get(self, index):
        return self.arr[index]

    def remove(self, index):
        self.arr[index] = None

    def contains(self, element):
        for i in self.arr:
            if i == element:
                return True
        
        return False

    def add(self, element):
        if self.index >= self.size:
            self.size += 10
            self.arr = Array(self.size)
        
        self.arr[self.index] = element
        self.index += 1

    def clear(self):
        for i in range(self.arr):
            self.arr[i] = None
        
        self.index = 0
    
    def size(self):
        return len(self.arr)
    
    def indexOf(self, element):
        for i in range(0, self.index):
            if self.arr[i] == element:
                return i
        return -1

    def display(self):
        self.arr.display()

