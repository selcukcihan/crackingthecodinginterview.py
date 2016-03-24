#! /usr/bin/env python
"""
How would you design a stack which, in addition to push and pop, also has a function
min which returns the minimum element? Push, pop and min should all operate in
O(1) time
"""

class MinStack:
    def __init__(self):
        self.total_size = 20
        self.buffer = [None] * self.total_size
        self.current = 0
        
    def push(self, item):
        if self.current == self.total_size:
            return False
        if self.current == 0:
            self.buffer[self.current] = (item, item)
        else:
            prev = self.buffer[self.current - 1]
            self.buffer[self.current] = (item, min(prev[1], item))
        self.current = self.current + 1
        return True
    
    def pop(self):
        if self.current == 0:
            return None
        self.current = self.current - 1
        item = self.buffer[self.current][0]
        return item
    
    def min(self):
        if self.current == 0:
            return None
        return self.buffer[self.current - 1][1]

def test_run():
    s = MinStack()
    s.push(5)
    s.push(7)
    s.push(1)
    s.push(9)
    
    print s.min()
    print s.pop()
    print s.min()
    print s.pop()
    print s.min()
    print s.pop()
    print s.min()
    print s.pop()
