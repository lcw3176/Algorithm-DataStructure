class Stack:
    def __init__(self):
        self.lst = []


    def __len__(self):
        return len(self.lst)


    def __str__(self):
        return str(self.lst[::1])


    def push(self, data):
        self.lst.append(data)


    def pop(self):
        if self.isEmpty():
            raise Exception("Empty Stack")

        return self.lst.pop()


    def clear(self):
        self.lst.clear()


    def contains(self, data):
        if self.isEmpty():
            raise Exception("Empty Stack")
        
        if data in self.lst:
            return True

        return False


    def peek(self):
        if self.isEmpty():
            raise Exception("Empty Stack")
        
        return self.lst.pop()


    def isEmpty(self):
        if len(self.lst) == 0:
            return True
        return False


    def size(self):
        return len(self.lst)