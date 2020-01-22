# A binary tree is a tree where each node has no more than two child nodes

# A binary search tree is a binary tree where for each node, the value of its 'left' child node must be less than the
# value of the node, and the value of the 'right' child node must be greater than or equal to the value of the node.
# This allows it to keep an ordered list of values, and adding and removing items is relatively quick.

# see also
# http://stackoverflow.com/questions/6380231/difference-between-binary-tree-and-binary-search-tree

# Note - the example in the book uses a simple 2D array (table) to store the tree, similar to an adjacency matrix
# for a graph. The code below creates an object for the tree and for each node

import random

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def traverse_pre_order(self):
        print(self.value)
        if self.left != None:
            self.left.traverse_pre_order()
        if self.right != None:
            self.right.traverse_pre_order()

    def traverse_in_order(self):
        if self.left != None:
            self.left.traverse_in_order()
        print(self.value)
        if self.right != None:
            self.right.traverse_in_order()

    def traverse_post_order(self):
        if self.left != None:
            self.left.traverse_post_order()
        if self.right != None:
            self.right.traverse_post_order()
        print(self.value)

    def traverse_in_order_advanced(self, visit_func, path):
        if self.left != None:
            self.left.traverse_in_order_advanced(visit_func, path+"L")
        visit_func(self.value, path)
        if self.right != None:
            self.right.traverse_in_order_advanced(visit_func, path+"R")

    def find(self, value, found_func, path):
        if self.value == value:
            found_func(path)
        elif self.left != None:
            self.left.find(value, found_func, path + "L")
        elif self.right != None:
            self.right.find(value, found_func, path + "R")

class BinarySearchTree:
    def __init__(self, value=None):
        if value is not None:
            self.insert(value)

    def insert(self, value):
        if not hasattr(self, 'root_node'):
            self.root_node = Node(value)
        else:
            self.root_node.insert(value)

    def traverse_pre_order(self):
        self.root_node.traverse_pre_order()

    def traverse_in_order(self):
        self.root_node.traverse_in_order()

    def traverse_post_order(self):
        self.root_node.traverse_post_order()

    def traverse_in_order_advanced(self, visit_func):
        self.root_node.traverse_in_order_advanced(visit_func, "")

    def find(self, value, found_func):
        self.root_node.find(value, found_func, '')


def generate_test_tree():
    tree = BinarySearchTree(50)

    tree.insert(10)
    tree.insert(-1)

    for i in range(0,20):
        number = random.randint(0,100)
        tree.insert(number)

    return tree

if __name__ == "__main__":
    my_tree = generate_test_tree()
    my_tree.traverse_in_order()
