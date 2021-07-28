class Heap:
    def __init__(self):
        self.item = [None]

    
    def push(self, data):
        self.item.append(data)
        i = len(self.item) - 1

        while i > 1:
            if self.item[i] > self.item[i // 2]:
                self.item[i], self.item[i // 2] = self.item[i // 2], self.item[i]
                i = i // 2
            else:
                break


    def pop(self):
        if len(self.item) < 1:
            raise IndexError("Empty heap")

        value = self.item[1]
        del self.item[1]
        self.heapify(1)
        return value
    

    def heapify(self, parent):
        left_child = 2 * parent
        right_child = 2 * parent + 1
        next_index = parent

        if left_child < len(self.item) and self.item[parent] < self.item[left_child]:
            next_index = left_child
        
        if right_child < len(self.item) and self.item[parent] < self.item[right_child]:
            next_index =right_child
        
        if next_index != parent:
            self.item[parent], self.item[next_index] = self.item[next_index], self.item[parent] 
            self.heapify(next_index)



    def __str__(self):
        return str(self.item[1::1])
