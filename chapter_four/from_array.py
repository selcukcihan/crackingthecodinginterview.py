#! /usr/bin/env python
"""
Given a sorted (increasing order) array, write an algorithm to create a binary tree with
minimal height.
"""

class BinaryTree:
    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            
        def __str__(self):
            return str(self.item)
    
    def __init__(self, items=None):
        self.root = None
        if items:
            self.create_from_sorted_array(items)
            
    def _from_array(self, items):
        if len(items) == 0:
            return None
        elif len(items) > 0:
            node = BinaryTree.Node(items[len(items) / 2])
            node.left = self._from_array(items[: len(items) / 2])
            node.right = self._from_array(items[(len(items) / 2) + 1 :])
            return node
    
    def create_from_sorted_array(self, items):
        self.root = self._from_array(items)
        
    def to_str_recursive(self, node):
        string = ""
        if node.left is not None:
            string += self.to_str_recursive(node.left)
        string += node.__str__()
        if node.right is not None:
            string += self.to_str_recursive(node.right)
        return string
        
    def __str__(self):
        if self.root is not None:
            return self.to_str_recursive(self.root)
        else:
            return ""

    def _height(self, node):
        if node is None:
            return 0
        left = self._height(node.left)
        right = self._height(node.right)
        return 1 + max(left, right)
        
    def height(self):
        return self._height(self.root)
                

def test_run():
    bt = BinaryTree(range(7))
    print bt
    print bt.height()
    
