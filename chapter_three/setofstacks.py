#! /usr/bin/env python
"""
Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Therefore,
in real life, we would likely start a new stack when the previous stack exceeds
some threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks
should be composed of several stacks, and should create a new stack once
the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop() should
behave identically to a single stack (that is, pop() should return the same values as it
would if there were just a single stack).
FOLLOW UP
Implement a function popAt(int index) which performs a pop operation on a specific
sub-stack
"""

class StackSet:
    class Stack:
        def __init__(self, size):
            self.size = size
            self.buffer = [None] * self.size
            self.current = 0
            
        def pop(self):
            if self.current > 0:
                self.current = self.current - 1
                return self.buffer[self.current]
            else:
                return None
                
        def push(self, item):
            if self.current == self.size:
                return False
            else:
                self.buffer[self.current] = item
                self.current = self.current + 1
                return True
                
    def __init__(self, size):
        self.size = size
        self.stacks = [self.Stack(size)]
    
    def push(self, item):
        if len(self.stacks) == 0:
            self.stacks.append(self.Stack(self.size))
        if not self.stacks[-1].push(item):
            self.stacks.append(self.Stack(self.size))
            self.stacks[-1].push(item)
            
    def pop(self):
        while len(self.stacks) > 0:
            item = self.stacks[-1].pop()
            if item is None:
                self.stacks.pop()
            else:
                return item

    def popAt(self, s):
        if s < len(self.stacks) and s >= 0:
            item = self.stacks[s].pop()
            if self.stacks[s].current == 0:
                del self.stacks[s]
            return item
        return None
        
def test_run():
    s = StackSet(3)
    print "pushing"
    [s.push(i) for i in range(15)]
    print "popping"
    while True:
        item = s.pop()
        if item is None:
            break
        print item
    print "pushing"
    [s.push(i) for i in range(10)]
    print "popping at 1"
    for i in range(3):
        item = s.popAt(1)
        print item
        
    print "popping at 2"
    print s.popAt(2)
    print "popping"
    while True:
        item = s.pop()
        if item is None:
            break
        print item    
        
