
class Node():
    def __init__(self, data):
        self.data = data
        self.lef = None
        self.right = None

    def __str__(self):
        return  str(self.data)

class BinaryTree():
    def __init__(self, data=None):
       if data:
            node = Node(data)
            self.root = node
       else:
           self.root= None
    def simetrical(self, node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end='')
            self.simetrical(node.left)
        print(node, end='')
        if node.right:
            self.simetrical(node.right)
            print(')', end='')


if __name__ == "__main__":
    tree = BinaryTree(9)
    tree.root.left = Node(18)
    tree.root.right = Node(21)

    print(tree.root)
    print(tree.root.right)
    print(tree.root.left)

