#! /usr/bin/env python
"""
Describe how you could use a single array to implement three stacks
"""

class NStack:
    def __init__(self, n, size):
        self.stacks = [{ 'beginning': s * size / n, 'current': s * size / n } for s in range(n)]
        self.buffer = [None] * size
    def push(self, s, item):
        if self.stacks[s]['current'] - self.stacks[s]['beginning'] == len(self.buffer) / len(self.stacks):
            return False
        else:
            self.buffer[self.stacks[s]['current']] = item
            self.stacks[s]['current'] = self.stacks[s]['current'] + 1

    def pop(self, s):
        if self.stacks[s]['current'] == self.stacks[s]['beginning']:
            return None
        else:
            self.stacks[s]['current'] = self.stacks[s]['current'] - 1
            return self.buffer[self.stacks[s]['current']]
    
    def print_values(self, s):
        print "-".join([str(s) for s in self.buffer[self.stacks[s]['beginning']:self.stacks[s]['current']]])

def test_run():
    stack = NStack(3, 15)
    stack.print_values(2)        
    for i in range(3):
        stack.push(0, i)
    for i in range(3,8):
        stack.push(1, i)
    for i in range(8,10):
        stack.push(2, i)

    stack.print_values(0)        
    stack.print_values(1)        
    stack.print_values(2)        

    print [stack.pop(0) for s in range(4)]
    print [stack.pop(1) for s in range(4)]
    print [stack.pop(2) for s in range(4)]
