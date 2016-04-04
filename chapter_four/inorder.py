#! /usr/bin/env python
"""
Write an algorithm to find the 'next' node (i.e., in-order successor) of a given node in
a binary search tree where each node has a link to its parent.
"""

from __future__ import print_function

class BinarySearchTree:
    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            self.parent = None
        def __str__(self):
            return str(self.item)

    def __init__(self, root_item):
        self.root = BinarySearchTree.Node(root_item)
        
    def add_left(self, parent, node):
        node.parent = parent
        parent.left = node
        
    def add_right(self, parent, node):
        node.parent = parent
        parent.right = node
        
    def _inorder(self, node):
        if node is not None:
            self._inorder(node.left)
            print(str(node.item) + "-", end="")
            self._inorder(node.right)
    def inorder(self):
        self._inorder(self.root)
        print("")

    def next(self, node):
        if node.right is not None: # has right subtree, next node should be there (the minimum element in that subtree)
            cur = node.right
            while cur.left is not None:
                cur = cur .left
            return cur
            
        elif node.parent is not None: # no right subtree, but has a parent, keep searching on the parent
            cur = node.parent
            prev = node
            while cur is not None:
                if cur.right is prev:
                    prev = cur
                    cur = cur.parent
                else:
                    break
            return cur
        
def test_run():
    bst = BinarySearchTree(10)
    bst.add_left(bst.root, BinarySearchTree.Node(5))
    bst.add_left(bst.root.left, BinarySearchTree.Node(3))
    bst.add_right(bst.root.left, BinarySearchTree.Node(8))
    bst.add_right(bst.root.left.right, BinarySearchTree.Node(9))
    bst.add_left(bst.root.left.left, BinarySearchTree.Node(1))
    
    bst.add_right(bst.root, BinarySearchTree.Node(15))
    
    print("inorder")
    bst.inorder()
    n = bst.next(bst.root.left.right.right)
    print(str(bst.root.left.right.right) + " -> " + str(n), end="\n")
    
    n = bst.next(bst.root)
    print(str(bst.root) + " -> " + str(n), end="\n")

    n = bst.next(bst.root.left)
    print(str(bst.root.left) + " -> " + str(n), end="\n")

    n = bst.next(bst.root.left.left.left)
    print(str(bst.root.left.left.left) + " -> " + str(n), end="\n")
    
