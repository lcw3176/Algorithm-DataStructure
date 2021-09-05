class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root = None):
        self.root = root


    def push(self, value):
        node = Node(value)
        tempNode = self.root

        if self.root is None:
            self.root = node
            return
        else:
            ptrNode = self.root
            while ptrNode is not None:
                tempNode = ptrNode

                if node.value < ptrNode.value:
                    ptrNode = ptrNode.left
                else:
                    ptrNode = ptrNode.right
            
            if node.value < tempNode.value:
                tempNode.left = node
            else:
                tempNode.right = node


    def remove(self, value):
        temp = self.root
        self.pop(temp, value)


    def pop(self, node, value):
        if node is None:
            return -1
        elif node.value > value:
            node.left = self.pop(node.left, value)
        elif node.value < value:
            node.right = self.pop(node.right, value)
        else:
            temp = node

            if node.right is None and node.left is None:
                del node
                node = None
            elif node.right is None:
                node = node.left
                del temp
            elif node.left is None:
                del temp
            else:
                temp = self.search_max_node()
                node.value = temp.value
                node.left = self.pop(node.left, temp.value)

            return node


    def search_max_node(self):
        if self.root is None:
            return
        else:
            temp = self.root
            maxVal = 0
            while temp is not None:
                maxVal = temp
                temp = temp.right
            
            return maxVal

    
    def show(self):
        temp = self.root
        self.in_order(temp)


    def in_order(self, node):
        if node is not None:
            self.in_order(node.left)
            print(node.value, end=" ")
            self.in_order(node.right)

    
    def pre_order(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)


    def post_order(self, node):
        if node is not None:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value, end=" ")