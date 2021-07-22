from linked_list import LinkedList

ls = LinkedList()
for i in range(10):
    ls.add(i)


for i in range(10):
    ls.remove(0)


for i in range(10):
    ls.add(i)


print(ls.contains(10))
print(ls.contains(2))
print(ls.get(1))
ls.display()
ls.clear()
ls.display()

for i in range(10):
    ls.add(i)

print(ls.size())
print(ls.indexOf(5))
print(ls.indexOf(100))
