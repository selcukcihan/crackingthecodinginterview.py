#! /usr/bin/env python
"""
Design an algorithm and write code to find the first common ancestor of two nodes
in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""

class BinaryTree:
    class Node:
        def __init__(self, item, parent=None):
            self.item = item
            self.parent = parent
            self.left = None
            self.right = None
        
        def __str__(self):
            return str(self.item)
            
    def __init__(self, item):
        self.root = BinaryTree.Node(item)
        
    def add_left(self, parent, item):
        parent.left = BinaryTree.Node(item, parent)

    def add_right(self, parent, item):
        parent.right = BinaryTree.Node(item, parent)
    
    def _inorder(self, node):
        if node is None:
            return ""
        else:
            return self._inorder(node.left) + "-" + str(node) + "-" + self._inorder(node.right)
            
    def inorder(self):
        return self._inorder(self.root)
        
    def first_common_ancestor_using_parent(self, first, second):
        f = first
        while f is not None:
            s = second
            while s is not None:
                if s is f:
                    return s
                s = s.parent
            f = f.parent
    
def test_run():
    bt = BinaryTree(10)
    bt.add_left(bt.root, 5)
    bt.add_left(bt.root.left, 19)
    bt.add_right(bt.root.left, 30)
    bt.add_right(bt.root, 0)
    bt.add_left(bt.root.left.right, 40)
    bt.add_right(bt.root.left.right, 50)
    bt.add_left(bt.root.right, 18)
    
    print bt.inorder()
    node = bt.first_common_ancestor_using_parent(bt.root.left.right.left, bt.root.left.right.right)
    print node
