class Array:
    def __init__(self, size):
        self.arr = [None for i in range(size)]
        self.size = size

    def __getitem__(self, key):
        if key > self.size:
            raise Exception("잘못된 인덱스로 값에 접근") 
        return self.arr[key]

    def __setitem__(self, key, value):
        if key > self.size:
            raise Exception("인덱스 초과")
        
        self.arr[key]= value
    
    def __len__(self):
        count = 0
        for i in self.arr:
            if i == None:
                break
            count += 1
        
        return count

    def display(self):
        temp = []
        for i in self.arr:
            if i == None:
                break
            temp.append(i)
        print(temp)

