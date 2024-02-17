# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 22:30:38 2024

@author: varung
"""

# Python3 program to convert a left 
# unbalanced BST to a balanced BST 
import sys
import math

# A binary tree node has data, pointer to left child 
# and a pointer to right child 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# This function traverse the skewed binary tree and 
# stores its nodes pointers in vector nodes[]
def storeBSTNodes(root, nodes):
    
    # Base case
    if not root:
        return
    
    # Store nodes in Inorder (which is sorted 
    # order for BST) 
    storeBSTNodes(root.left, nodes)
    nodes.append(root)
    storeBSTNodes(root.right, nodes)

# Recursive function to construct binary tree 
def buildTreeUtil(nodes, start, end):
    
    # base case 
    if start > end:
        return None

    # Get the middle element and make it root 
    mid = (start + end) // 2
    node = nodes[mid]

    # Using index in Inorder traversal, construct 
    # left and right subtrees
    node.left = buildTreeUtil(nodes, start, mid - 1)
    node.right = buildTreeUtil(nodes, mid + 1, end)
    return node

# This functions converts an unbalanced BST to 
# a balanced BST
def buildTree(root):
    
    # Store nodes of given BST in sorted order 
    nodes = []
    storeBSTNodes(root, nodes)

    # Constructs BST from nodes[] 
    n = len(nodes)
    return buildTreeUtil(nodes, 0, n - 1)

# Function to do preorder traversal of tree
def preOrder(root):
    if not root:
        return
    print("{} ".format(root.data), end="")
    preOrder(root.left)
    preOrder(root.right)

# Driver code
if __name__ == '__main__':
    # Constructed unbalanced binary tree is 
    #         4
    #        / \
    #       3   5
    #      /     \
    #     2       6 
    #    /         \
    #   1           7
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.left.left = Node(1)
    root.right = Node(5)
    root.right.right = Node(6)
    root.right.right.right = Node(7)

    root = buildTree(root)
    print("Preorder traversal of balanced BST is :")
    preOrder(root)
