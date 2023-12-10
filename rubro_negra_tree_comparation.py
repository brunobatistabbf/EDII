import random
import time

class Node:
    def __init__(self, key, color='RED'):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.color = color

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, color='BLACK')
        self.root = self.NIL

    def rotate_left(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def rotate_right(self, y):
        x = y.left
        y.left = x.right

        if x.right != self.NIL:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        x.right = y
        y.parent = x

    def insert_fixup(self, z):
        while z.parent is not None and z.parent.color == 'RED':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y is not None and y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        if z.parent is not None:
                            self.rotate_left(z)
                    if z.parent is not None and z.parent.parent is not None:
                        if z.parent.parent.left != self.NIL:
                            z.parent.color = 'BLACK'
                            z.parent.parent.color = 'RED'
                            self.rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y is not None and y.color == 'RED':
                    z.parent.color = 'BLACK'
                    y.color = 'BLACK'
                    z.parent.parent.color = 'RED'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        if z.parent is not None:
                            self.rotate_right(z)
                    if z.parent is not None and z.parent.parent is not None:
                        if z.parent.parent.right != self.NIL:
                            z.parent.color = 'BLACK'
                            z.parent.parent.color = 'RED'
                            self.rotate_left(z.parent.parent)
        self.root.color = 'BLACK'

    def insert(self, key):
        new_node = Node(key)
        y = self.NIL
        x = self.root

        while x != self.NIL:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.parent = y
        if y == self.NIL:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.color = 'RED'

        if y != self.NIL:
            self.insert_fixup(new_node)

    def remove(self, key):
        node = self._search(key)
        if node != self.NIL:
            self._remove(node)

    def _search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search_recursive(node.left, key)
        return self._search_recursive(node.right, key)

    def _remove(self, node):
        y = node
        y_original_color = y.color
        if node.left == self.NIL:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.NIL:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color
            x = y.right
            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y
            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color
        if y_original_color == 'BLACK':
            self._remove_fixup(x)

    def _transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def _remove_fixup(self, x):
        while x != self.root and x.color == 'BLACK':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == 'BLACK' and w.right.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.right.color == 'BLACK':
                        w.left.color = 'BLACK'
                        w.color = 'RED'
                        self.rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.right.color = 'BLACK'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'RED':
                    w.color = 'BLACK'
                    x.parent.color = 'RED'
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == 'BLACK' and w.left.color == 'BLACK':
                    w.color = 'RED'
                    x = x.parent
                else:
                    if w.left.color == 'BLACK':
                        w.right.color = 'BLACK'
                        w.color = 'RED'
                        self.rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'BLACK'
                    w.left.color = 'BLACK'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'BLACK'

    def _minimum(self, node):
        while node.left != self.NIL:
            node = node.left
        return node

    def count_occurrences(self, key):
        return self._count_occurrences_recursive(self.root, key)

    def _count_occurrences_recursive(self, node, key):
        if node == self.NIL:
            return 0
        count = self._count_occurrences_recursive(node.left, key) + self._count_occurrences_recursive(node.right, key)
        if node.key == key:
            count += 1
        return count

    def in_order_traversal(self, node):
        result = []
        if node != self.NIL:
            result.extend(self.in_order_traversal(node.left))
            result.append(node.key)
            result.extend(self.in_order_traversal(node.right))
        return result

    def get_sorted_elements(self):
        return self.in_order_traversal(self.root)

if __name__ == "__main__":
    rb_tree = RedBlackTree()

    start_all = time.time()
    start_insert = time.time()

    with open('dados100_mil.txt', 'r') as arquivo:
        data = [int(numero) for numero in arquivo.read().strip('[]').split(', ')]
    for number in data:
        rb_tree.insert(number)
    final_insert =time.time()
    print(f"Tempo para preencher a árvore: {final_insert - start_insert} segundos")


    random_numbers = random.sample(range(-9999, 10000), min(50000, 19999))


    for number in random_numbers:
        if number % 3 == 0:
            rb_tree.insert(number)
        elif number % 5 == 0:
            rb_tree.remove(number)
        else:
            count = rb_tree.count_occurrences(number)
            print(f"O número {number} aparece {count} vezes na árvore.")


    sorted_elements = rb_tree.get_sorted_elements()
    print("Dados da Árvore:\n", sorted_elements)
    final_all = time.time()
    print(f"Tempo total da operação: {final_all - start_all} segundos")



