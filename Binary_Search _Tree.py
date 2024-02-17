# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:30:11 2024

@author: varung
"""

class Node:
    # Constructor to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# A utility function to insert
# a new node with the given key in BST
def insert(node, key):
    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    elif key > node.key:
        node.right = insert(node.right, key)

    # Return the (unchanged) node pointer
    return node

# Utility function to search a key in a BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.key == key:
        return root

    # Key is greater than root's key
    if root.key < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)

# Driver Code
if __name__ == '__main__':
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    # Key to be found
    key_to_find = 80

    # Searching in a BST
    if search(root, key_to_find) is not None:
        print(f"Element {key_to_find} found in the BST.")
    else:
        print(f"Element {key_to_find} not found in the BST.")

    key_to_find = 10

    # Searching in a BST
    if search(root, key_to_find) is not None:
        print(f"Element {key_to_find} found in the BST.")
    else:
        print(f"Element {key_to_find} not found in the BST.")
