#! /usr/bin/env python
"""
You have two very large binary trees: T1, with millions of nodes, and T2, with hundreds
of nodes. Create an algorithm to decide if T2 is a subtree of T1.
"""

class BinaryTree:

    class Node:
        def __init__(self, item):
            self.item = item
            self.left = None
            self.right = None
            
        def __str__(self):
            return str(self.item)

            
    def __init__(self, items):
        self.root = self._recursive_init(items)

    def _recursive_init(self, items):
        length = len(items)
        if length == 0:
            return None
        node = BinaryTree.Node(items[length // 2])
        node.left = self._recursive_init(items[: (length // 2)])
        node.right = self._recursive_init(items[(length // 2) + 1 :])
        return node

    def _inorder(self, node):
        if node is None:
            return ""
        return self._inorder(node.left) + "-" + str(node) + self._inorder(node.right)    

    def __str__(self):
        return self._inorder(self.root)
    
    def is_subtree_of(self, bigtree):
        stack = [bigtree.root]
        while len(stack) > 0:
            node = stack.pop()
            stack_big = [(node, 0)]
            stack_self = [(self.root, 0)]
            subtree = True
            while len(stack_big) > 0:
                big_node = stack_big.pop()
                self_node = stack_self.pop()
                if big_node[0].item != self_node[0].item or big_node[1] != self_node[1]:
                    subtree = False
                    break
                if big_node[0].left is not None:
                    stack_big.append((big_node[0].left, big_node[1] + 1))
                if big_node[0].right is not None:
                    stack_big.append((big_node[0].right, big_node[1] + 1))
                if self_node[0].left is not None:
                    stack_self.append((self_node[0].left, self_node[1] + 1))
                if self_node[0].right is not None:
                    stack_self.append((self_node[0].right, self_node[1] + 1))
            if subtree:
                return True
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        return False
    
def test_run():
    small = BinaryTree(range(3))
    print small
    big = BinaryTree(range(6))
    print big
    print small.is_subtree_of(big)
    
