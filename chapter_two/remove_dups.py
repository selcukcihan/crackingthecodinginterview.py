#! /usr/bin/env python
"""
"""
# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# a -> b -> a -> c -> a -> d -> d

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
        arr = []
        while (n is not None):
            arr.append(n.char + " (" + str(id(n)) + ")")
            n = n.next
        return " --> ".join(arr)
        
    def remove_duplicates(self):
        chars = set()
        cur = self.head
        prev = None
        while cur is not None:
            if cur.char in chars:
                prev.next = cur.next
            else:
                chars.add(cur.char)
            prev = cur
            cur = cur.next

    def remove_duplicates_no_buffer(self):
        candidate = self.head
        while candidate is not None:
            cur = candidate.next
            prev = candidate
            while cur is not None:
                if cur.char == candidate.char:
                    prev.next = cur.next
                prev = cur
                cur = cur.next
            candidate = candidate.next

def test_run():
    lst = LinkedList()
    lst.append('a').append('b').append('c').append('a').append('d').append('c')
    print lst
    lst.remove_duplicates()
    print lst
    
    lst = LinkedList()
    lst.append('a').append('b').append('c').append('a').append('d').append('c')
    print lst
    lst.remove_duplicates_no_buffer()
    print lst

