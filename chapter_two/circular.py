#! /usr/bin/env python
"""
Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an
earlier node, so as to make a loop in the linked list.
EXAMPLE
input: A -> B -> C -> D -> E -> C [the same C as earlier]
output: C
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
    def tie(self, n):
        if self.tail is not None:
            self.tail.next = n
        
    def __str__(self):
        n = self.head
        digits = []
        while (n is not None):
            digits.append(str(n.char))
            if n is self.tail:
                break
            n = n.next
        return " --> ".join(digits)
        
def find_beginning_of_loop(lst):
    visited = set()
    n = lst.head
    while n is not None:
        if n in visited:
            return n
        visited.add(n)
        n = n.next
    return None
       
def find_beginning_of_loop_no_set(lst):
    t = lst.head
    r = lst.head
    counter = 0
    while True:
        t = t.next # tortoise has 1x speed
        r = r.next.next # rabbit has 2x speed
        counter = counter + 1
        if t is r: # rabbit overlapping tortoise
            break
    t = lst.head
    while t is not r:
        t = t.next
        r = r.next
    return t
            
        

def test_run():
    lst1 = LinkedList()
    #lst1.append(5).append(1).append(8).append(4)
    #lst1.tie(lst1.head.next)
    for i in range(20):
        lst1.append(i)
    n = lst1.head
    for j in range(15):
        n = n.next
    lst1.tie(n)
    print lst1
    n = find_beginning_of_loop(lst1)
    print n.char
    n = find_beginning_of_loop_no_set(lst1)
    print n.char

