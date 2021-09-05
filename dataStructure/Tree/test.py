from tree import BinaryTree

tr = BinaryTree()
for i in range(40, 60):
    tr.push(i)

for i in range(20, 30):
    tr.push(i)
tr.show()
print()
print(tr.search_max_node().value)

