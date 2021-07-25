class Queue:
    def __init__(self, size):
        self.item = [0 for i in range(size)]
        self.front = 0
        self.rear = 0
        self.init_size = size


    def enqueue(self, data):
        if self.full():
            raise IndexError("Full queue")
        self.item[self.rear] = data
        self.rear += 1


    def dequeue(self):
        if self.empty():
            raise IndexError("Empty queue")

        value = self.item[self.front]
        for i in range(self.front + 1, self.rear):
            self.item[i - 1] = self.item[i]
        
        self.rear -= 1
        del self.item[self.rear]


        return value


    def empty(self):
        if self.front == self.rear:
            return True
        return False


    def size(self):
        return len(self.item)


    def peek(self):
        if self.empty():
            raise IndexError("Empty queue")

        return self.item[self.front]


    def full(self):
        if self.init_size == self.rear:
            return True
        return False


    def __len__(self):
        return self.rear


    def __str__(self):
        return str(self.item[::1])