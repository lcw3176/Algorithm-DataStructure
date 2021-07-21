class Array:
    def __init__(self, size):
        self.arr = [None for i in range(size)]
        self.count = 0

    def __getitem__(self, key):
        if key > self.count:
            raise Exception("잘못된 인덱스로 값에 접근") 
        return self.arr[key]

    def __setitem__(self, key, value):
        if key > self.count:
            raise Exception("인덱스 초과")

        self.arr[key]= value
        self.count += 1

    def display(self):
        temp = []
        for i in self.arr:
            if i == None:
                break
            temp.append(i)
        print(temp)

