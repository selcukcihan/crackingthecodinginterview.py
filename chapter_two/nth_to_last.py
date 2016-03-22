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
        
    def nth_to_last(self, n):
        if n < 1:
            return None
        queue = deque(maxlen=n)
        cur = self.head
        count = 0
        while cur is not None:
            queue.append(cur)
            count = count + 1
            cur = cur.next
        item = None
        if count >= n:
            while n > 0:
                item = queue.pop()
                n = n - 1
        return item

    def nth_to_last_elegant(self, n):
        candidate = self.head
        cur = self.head
        count = 0
        while cur is not None:
            cur = cur.next
            count = count + 1
            if count >= n:
                candidate = candidate.next
        if count >= n:
            return candidate
        else:
            return None
        
def test_run():
    lst = LinkedList()
    lst.append('a').append('b').append('c').append('a').append('d').append('c')
    print lst
    print lst.nth_to_last(2).char
    print lst.nth_to_last(3).char
    print lst.nth_to_last(1).char

    print lst.nth_to_last_elegant(2).char
    print lst.nth_to_last_elegant(3).char
    print lst.nth_to_last_elegant(1).char

