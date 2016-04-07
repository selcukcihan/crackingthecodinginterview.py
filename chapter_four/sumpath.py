#! /usr/bin/env python
"""
You are given a binary tree in which each node contains a value. Design an algorithm
to print all paths which sum up to that value. Note that it can be any path in the tree
- it does not have to start at the root.
"""

from random import randint

class BinaryTree:
    class Node:
        def __init__(self, item):
            self.item = item
        def __str__(self):
            return str(self.item)
    
    def _recursive_init(self, items):
        length = len(items)
        if length == 0:
            return None
        node = BinaryTree.Node(items[length // 2])
        node.left = self._recursive_init(items[: (length // 2)])
        node.right = self._recursive_init(items[(length // 2) + 1 :])
        return node
        
    def __init__(self, items):
        self.root = self._recursive_init(items)
    
    def _inorder(self, node):
        if node is None:
            return ""
        return self._inorder(node.left) + "." + str(node) + self._inorder(node.right)
        
    def __str__(self):    
        return self._inorder(self.root)

    def _paths_summing_up_to(self, node, paths, value):
        if node is None:
            return []
        retval = []
        mypaths = []
        for path in paths + [[]]:
            mypaths.append(path + [node])
            total = 0
            for n in mypaths[-1]:
                total += n.item
            if total == value:
                retval.append(mypaths[-1])

        retval.extend(self._paths_summing_up_to(node.left, mypaths, value))
        retval.extend(self._paths_summing_up_to(node.right, mypaths, value))
        return retval
        
    def paths_summing_up_to(self, value):
        return self._paths_summing_up_to(self.root, [], value)
            
        
def test_run():
    #tree = BinaryTree([randint(0, 9) for i in range(50)])
    tree = BinaryTree([1, 2, 2, 2, 1, 1, 4, -1, 5])
    print tree
    paths = tree.paths_summing_up_to(5)
    for path in paths:
        p = ""
        for n in path:
            p = p + str(n) + "."
        print p

