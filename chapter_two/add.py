#! /usr/bin/env python
"""
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such tat the 1's digit is at the head of
the list. Write a function that adds the two numbers and returns the sum as a linked list
EXAMPLE
Input: (3 -> 1 -> 5) + (5 -> 9 -> 2)
Output: 8 -> 0 -> 8
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
        digits = []
        while (n is not None):
            digits.append(str(n.char))
            n = n.next
        return " --> ".join(digits)
        
def add(lst1, lst2):
    lst = LinkedList()
    p1 = lst1.head
    p2 = lst2.head
    carry = 0
    while p1 is not None and p2 is not None:
        digit = p1.char + p2.char + carry
        lst.append(digit % 10)
        carry = digit / 10
        p1 = p1.next
        p2 = p2.next
    p = p1 if p1  is not None else p2
    if p is not None:
        digit = p.char + carry
        lst.append(digit % 10)
        carry = digit / 10        
        p = p.next
    if carry > 0:
        lst.append(carry)
    return lst
        
def test_run():
    lst1 = LinkedList()
    lst1.append(5).append(1).append(8)
    lst2 = LinkedList()
    lst2.append(7).append(1)
    print lst1
    print lst2
    lst = add(lst1, lst2)
    print lst
    lst = add(lst2, lst1)
    print lst

