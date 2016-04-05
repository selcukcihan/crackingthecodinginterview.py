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

    def _fce(self, nodes, current):
        retval = [False, False, None]
        if current is not None:
            left = self._fce(nodes, current.left)
            right = self._fce(nodes, current.right)
            
            if left[0] and left[1]: # both nodes are contained in the left subtree
                return left
            elif right[0] and right[1]: # both nodes are contained in the right subtree
                return right
            if (left[0] or right[0]) and (left[1] or right[1]):
                return [True, True, current]
            retval[0] = retval[0] or (left[0] or right[0])
            retval[1] = retval[1] or (left[1] or right[1])
                
            if current in nodes:
                retval[nodes.index(current)] = True
        return retval
        
    def first_common_ancestor(self, first, second):
        return self._fce([first, second], self.root)[2]
    
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

    #node = bt.first_common_ancestor_using_parent(bt.root.left.right.right, bt.root.left.left)
    node = bt.first_common_ancestor_using_parent(bt.root.left.right.right, bt.root.right)
    print node

    #node = bt.first_common_ancestor(bt.root.left.right.right, bt.root.left.left)
    node = bt.first_common_ancestor(bt.root.left.right.right, bt.root.right)
    print node
    
