from queue import Queue

que = Queue(100)
for i in range(100):
    que.enqueue(i)

# que.enqueue(101) # IndexError: Full queue
print(que.full()) # True
print(que.size()) # 100
print(que.empty()) # False
print(que.peek()) # 0

for i in range(100):
    que.dequeue()

print(que.size()) # 0
print(que.empty()) # True
# print(que.peek()) # Exception: Empty Queue
