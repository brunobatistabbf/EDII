class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def balance(self, node):
        if node is None:
            return 0

        self.update_height(node)

        balance = self.balance_factor(node)


        if balance > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            return root

        return self.balance(root)

    def insert_file_data(self):
        with open('dados100_mil.txt', 'r') as arquivo:
            data = [int(numero) for numero in arquivo.read().strip('[]').split(', ')]

        for value in data:
            self.root = self.insert(self.root, value)

    def remove_multiples(self, root, multiple):
        if root is None:
            return None

        if root.key % multiple == 0:
            return self.remove_multiples(self.remove(root, root.key), multiple)

        root.left = self.remove_multiples(root.left, multiple)
        root.right = self.remove_multiples(root.right, multiple)

        return root

    def count_occurrences(self, root, value):
        if root is None:
            return 0

        count = 0
        if root.key == value:
            count += 1

        count += self.count_occurrences(root.left, value)
        count += self.count_occurrences(root.right, value)

        return count

    def remove(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.remove(root.left, key)
        elif key > root.key:
            root.right = self.remove(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left


            root.key = self.get_min_value_node(root.right).key
            root.right = self.remove(root.right, root.key)

        return self.balance(root)

    def get_min_value_node(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def print_tree(self, root):
        if root is not None:
            self.print_tree(root.left)
            print(root.key, end=' ')
            self.print_tree(root.right)


if __name__ == "__main__":
    avl_tree = AVLTree()

    import time

    start_time_all = time.time()
    start_time = time.time()
    avl_tree.insert_file_data()
    end_time = time.time()

    print(f"Tempo para preencher a árvore: {end_time - start_time} segundos")

    import random

    for _ in range(50000):
        random_number = random.randint(-9999, 9999)
        if random_number % 3 == 0:
            avl_tree.root = avl_tree.insert(avl_tree.root, random_number)
        elif random_number % 5 == 0:
            avl_tree.root = avl_tree.remove_multiples(avl_tree.root, 5)
        else:
            occurrences = avl_tree.count_occurrences(avl_tree.root, random_number)
            print(f"O número {random_number} aparece {occurrences} vezes na árvore.")

    print("\nDados da árvore AVL:")
    avl_tree.print_tree(avl_tree.root)
    end_time_all = time.time()
    print(f"Tempo total da operação: {end_time_all - start_time_all} segundos")