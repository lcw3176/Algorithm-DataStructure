from stack import Stack

st = Stack()

for i in range(10):
    st.push(i) 

print(st) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(5):
    print(st.pop(), end=" ") # 9 8 7 6 5 
print()

for i in range(5):
    print(st.peek(), end=" ") # 4 3 2 1 0 
print()

print(st.isEmpty()) # True

for i in range(10):
    st.push(i)

print(st.isEmpty()) # False
st.clear()
print(st.isEmpty()) # True
print(st.size()) # 0
# st.contains(0) # Exception: Empty Stack

for i in range(10):
    st.push(i)

print(st.contains(4)) # True