#! /usr/bin/env python
"""
Implement a function to check if a tree is balanced. For the purposes of this question,
a balanced tree is defined to be a tree such that no two leaf nodes differ in distance
from the root by more than one.
"""

class Node:
    def __init__(self, item, children=None):
        self.item = item
        self.children = children if children is not None else []
    def __str__(self):
        return str(self.item)

    def add(self, child):
        node = Node(child)
        self.children.append(node)
        return self
        
class Tree:
    class CurrentMinMax:
        def __init__(self):
            self.minimum = None
            self.maximum = None
    def __init__(self, item):
        self.root = Node(item)
    
    def _is_balanced(self, current_node, current_level, minmax):
        if current_node is not None:
            if len(current_node.children) == 0:
                if minmax.minimum is None or current_level < minmax.minimum:
                    minmax.minimum = current_level
                if minmax.maximum is None or current_level > minmax.maximum:
                    minmax.maximum = current_level
                if minmax.maximum - minmax.minimum > 1:
                    return False
            for c in current_node.children:
                if not self._is_balanced(c, current_level + 1, minmax):
                    return False
        return True
            
    def is_balanced(self):
        return self._is_balanced(self.root, 0, Tree.CurrentMinMax())
        
def inorder(node):
    if node is not None:
        print node.item
        for c in node.children:
            inorder(c)
        
def test_run():
    tree = Tree(1)
    tree.root.add(2).add(3).add(4)
    tree.root.children[0].add(5).add(6)
    tree.root.children[0].children[1].add(10)

    
    print "tree:"
    inorder(tree.root)
    
    print "is balanced"
    print tree.is_balanced()
