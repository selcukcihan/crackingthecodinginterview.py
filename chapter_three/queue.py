#! /usr/bin/env python
"""
Implement a MyQueue class which implements a queue using two stacks
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

class Queue:
    def __init__(self):
        self.s1 = NStack(1, 20)
        self.s2 = NStack(1, 20)
    def enqueue(self, item):
        self.s1.push(0, item)
        return self
    def dequeue(self):
        item = self.s2.pop(0)
        if item is None:
            while True:
                tmp = self.s1.pop(0)
                if tmp is None:
                    break
                self.s2.push(0, tmp)
            item = self.s2.pop(0)
        return item


def test_run():
    q = Queue()
    q.enqueue(1).enqueue(2).enqueue(3)
    print q.dequeue()
    print q.dequeue()
    q.enqueue(4).enqueue(5).enqueue(6).enqueue(7)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    q.enqueue(10).enqueue(20).enqueue(30)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()

