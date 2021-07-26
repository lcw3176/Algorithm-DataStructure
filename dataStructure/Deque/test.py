from deque import Deque

de = Deque()

for i in range(10):
    de.push_front(i)

for i in range(10):
    print(de.pop_front(), end=" ") # 9 8 7 6 5 4 3 2 1 0 
print()


for i in range(10):
    de.push_back(i)

print(de.empty()) # False


for i in range(10):
    print(de.pop_back(), end=" ") # 9 8 7 6 5 4 3 2 1 0
print()

print(de.empty()) # True

for i in range(5):
    de.push_front(i)

for i in range(5):
    de.push_back(i)


for i in range(10):
    print(de.pop_front(), end=" ") # 4 3 2 1 0 0 1 2 3 4
