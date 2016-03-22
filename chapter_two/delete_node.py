#! /usr/bin/env python
"""
Implement an algorithm to find the nth to last element of a singly linked list
"""

from collections import deque

class Node:
    def __init__(self, char):
        self.char = char
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def append(self, char):
        if self.tail is None:
            self.head = self.tail = Node(char)
            return self
        else:
            self.tail.next = Node(char)
            self.tail = self.tail.next
            return self
        
    def __str__(self):
        n = self.head
        str = []
        while (n is not None):
            str.append(n.char)
            n = n.next
        return " --> ".join(str)
        
    def delete_node(self, n):
        if n is None or n.next is None:
            return False
        else:
            n.char = n.next.char
            n.next = n.next.next
            return True
        
def test_run():
    lst = LinkedList()
    lst.append('a').append('b').append('c').append('a').append('d').append('c')
    print lst
    lst.delete_node(lst.head.next.next)
    print lst

