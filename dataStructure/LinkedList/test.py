from linked_list import LinkedList

ls = LinkedList()
for i in range(100):
    ls.add(i)

ls.display()

for i in range(20):
    ls.remove(15)

ls.display()

for i in range(100, 120):
    ls.add(i)

ls.display()

print(ls.contains(10))
print(ls.contains(2))
print(ls.get(1))
ls.display()
ls.clear()

for i in range(100):
    ls.add(i)

print(ls.size())
print(ls.indexOf(5))
print(ls.indexOf(125))
ls.display()
