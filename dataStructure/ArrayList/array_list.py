from c_array import Array


class ArrayList:
    def __init__(self):
        self.count = 10
        self.index = 0
        self.arr = Array(self.count)

    def get(self, index):
        if index >= self.index:
            raise Exception("인덱스 초과")

        return self.arr[index]

    def remove(self, index):
        self.arr[index] = None
        for i in range(index, len(self.arr) - 1):
            self.arr[i] = self.arr[i + 1]

        self.index = len(self.arr) - 1

    def contains(self, element):
        for i in self.arr:
            if i == element:
                return True
        
        return False

    def add(self, element):
        if self.index >= self.count:
            self.count *= 2
            temp = self.arr
            self.arr = Array(self.count)

            for i in range(len(temp)):
                self.arr[i] = temp[i]
        
        self.arr[self.index] = element
        self.index += 1

    def clear(self):
        for i in range(len(self.arr)):
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

