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


class NStackAdvanced:
    class StackMeta:
        def __init__(self):
            self.count = 0
            self.top = None
        
    def __init__(self, n, size):
        self.count = 0
        self.size = size
        self.buffer = [None] * size
        self.stacks = [self.StackMeta() for s in range(n)]
        self.empty_slots = [(0, size)]

        
    def push(self, s, item):
        if self.count == self.size:
            return False
        else:
            target = self.empty_slots[0][0] # we will put the item in that index
            self.empty_slots[0] = (self.empty_slots[0][0] + 1, self.empty_slots[0][1] - 1) # one empty slot gone
            if self.empty_slots[0][1] == 0: # if the consecutive empty slots vanished, we delete it from the list
                del self.empty_slots[0]
            
            self.buffer[target] = item # put the item in the buffer
            
            # maintain the link of that individual stack s
            if self.stacks[s].top is None:
                self.stacks[s].top = (target, None)
            else:
                self.stacks[s].top = (target, self.stacks[s].top)
            # increment item counters
            self.stacks[s].count = self.stacks[s].count + 1
            self.count = self.count + 1
            
    def pop(self, s):
        if self.stacks[s].count == 0:
            return None
        else:
            item = self.buffer[self.stacks[s].top[0]]
            
            self.empty_slots.append((self.stacks[s].top[0], 1))
            self.stacks[s].top = self.stacks[s].top[1]
            
            # decrement item counters
            self.stacks[s].count = self.stacks[s].count - 1
            self.count = self.count - 1
            
            return item
            
def test_run2():
    s = NStackAdvanced(3, 15)
    [s.push(0, i) for i in range(30)]
    [s.push(1, i) for i in range(3, 10)]
    [s.push(1, i) for i in range(6)]
    s.push(1, 20)
    s.push(2, 20)
    for i in range(3):
        print "in: " + str(i)
        while True:
            item = s.pop(i)
            if item is None:
                break
            print item

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
