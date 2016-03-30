#! /usr/bin/env python
"""
Write a program to sort a stack in ascending order. You should not make any assumptions
about how the stack is implemented. The following are the only functions that
should be used to write this program: push | pop | peek | isEmpty.
"""

class Stack:
    def __init__(self):
        self.buffer = []
    def pop(self):
        item = self.buffer[-1]
        del self.buffer[-1]
        return item
    def peek(self):
        return self.buffer[-1]
    def push(self, item):
        self.buffer.append(item)
        return self
    def is_empty(self):
        return len(self.buffer) == 0

class SortedStack(Stack):
    def __init__(self):
        Stack.__init__(self)
    def sort(self):
        s = Stack()
        total = len(self.buffer)
        source = self
        target = s
        carry = None
        for i in range(total, 0, -1):
            min_item = None
            for j in range(i):
                item = source.pop()
                if min_item is None:
                    min_item = item
                elif item < min_item:
                    target.push(min_item)
                    min_item = item
                else:
                    target.push(item)
            if carry is not None:
                self.push(carry)
                carry = None
            if target is self:
                carry = min_item
            else:
                self.push(min_item)
            
            tmp = source
            source = target
            target = tmp

        self.buffer = target.buffer if len(target.buffer) > 0 else source.buffer
        if carry is not None:
            self.push(carry)
            
            
def test_run():
    s = SortedStack()
    s.push(15).push(7).push(1).push(3).push(10)
    print s.buffer
    s.sort()
    print s.buffer
    
