#! /usr/bin/env python
"""
Given a binary search tree, design an algorithm which creates a linked list of all the
nodes at each depth (i.e., if you have a tree with depth D, you'll have D linked lists).
"""

class BinarySearchTree:
    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
        def __str__(self):
            return str(self.item)
            
    def __init__(self):
        self.root = None
    
    def preorder(self):
        print self._preorder(self.root)

    def _preorder(self, node):
        result = ""
        if node is not None:
            result += self._preorder(node.left)
            result += node.__str__() + " - "
            result += self._preorder(node.right)
        return result

class LinkedList:
    class Node:
        def __init__(self, node):
            self.node = node
            self.next = None
            
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
    def __str__(self):
        n = self.head
        result = ""
        while n is not None:
            result += (n.node.__str__() + " - ")
            n = n.next
        return result
        
    def append(self, node):
        if node is not None:
            if self.head is not None:
                self.tail.next = LinkedList.Node(node)
                self.tail = self.tail.next
            else:
                self.tail = self.head = LinkedList.Node(node)
            self.count += 1
            return self.tail
        else:
            return None
            
def create_level_lists(tree):
    level = LinkedList()
    level.append(tree.root)
    lst = []
    while True:
        lst.append(level)
        next_level = LinkedList()
        n = level.head
        while n is not None:
            if n.node.left is not None:
                next_level.append(n.node.left)
            if n.node.right is not None:
                next_level.append(n.node.right)
            n = n.next
        if next_level.count == 0:
            break
        level = next_level

    return lst

def test_run():
    tree = BinarySearchTree()

    tree.root = BinarySearchTree.Node(10)

    tree.root.left = BinarySearchTree.Node(5)
    tree.root.right = BinarySearchTree.Node(15)

    tree.root.left.right = BinarySearchTree.Node(8)
    tree.root.right.left = BinarySearchTree.Node(13)
    tree.root.right.right = BinarySearchTree.Node(14)

    tree.root.left.right.left = BinarySearchTree.Node(6)
    tree.root.right.left.left = BinarySearchTree.Node(11)

    tree.root.right.left.left.right = BinarySearchTree.Node(12)
    
    print "tree:"
    tree.preorder()
    
    lst = create_level_lists(tree)
    for l in lst:
        print l.__str__()
