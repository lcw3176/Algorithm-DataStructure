class HashTableWithChain:
    def __init__(self, size):
        self.bucket = [0 for i in range(size)]
        self.size = size

    def put(self, key, value):
        hash = self.hashFunction(key)
        
        if self.bucket[hash] != 0:
            if type(self.bucket[hash]) == list:
                self.bucket[hash].append(value)
            else:
                temp = self.bucket[hash]
                self.bucket[hash] = []
                self.bucket[hash].append(temp)
                self.bucket[hash].append(value)

        else:
            self.bucket[hash] = value
    def get(self, key):
        hash = self.hashFunction(key)
        return self.bucket[hash]
    
    def hashFunction(self, key):
        return key % self.size

    def show(self):
        print(self.bucket)


hash = HashTableWithChain(10)
for i in range(10):
    hash.put(i, "hello")
print(hash.get(1)) ## hello
hash.put(0, "hello")
hash.show() ## [['hello', 'hello'], 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello', 'hello']