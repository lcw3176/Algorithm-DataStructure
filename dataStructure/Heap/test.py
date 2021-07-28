from heap import Heap
import random

hp = Heap()
for _ in range(10):
    hp.push(random.randrange(1, 10)) 
print(hp)

for _ in range(10):
    print(hp.pop())
