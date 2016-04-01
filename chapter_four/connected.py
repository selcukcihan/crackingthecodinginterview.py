#! /usr/bin/env python
"""
Given a directed graph, design an algorithm to find out whether there is a route between
two nodes.
"""

class DiGraph:
    class Node:
        def __init__(self, item):
            self.item = item
            self.adj = []
        def __str__(self):
            return str(item)
            
    def __init__(self):
        self.nodes = {}

    def _get_or_add(self, item):
        if item not in self.nodes:
            self.nodes[item] = DiGraph.Node(item)
        return self.nodes[item]
        
    def connect(self, item1, item2):
        self._get_or_add(item1).adj.append(self._get_or_add(item2))

    def is_connected_recursive(self, s, t):
        if self.nodes[s] is self.nodes[t]:
            return True
        else:
            for n in self.nodes[s].adj:
                if self.is_connected(n.item, t):
                    return True
            return False

    def is_connected(self, s, t):
        s = self.nodes[s]
        t = self.nodes[t]
        queue = []
        visited = set()
        queue.append(s)
        while queue:
            n = queue.pop()
            if n in visited:
                continue
            if n is t:
                return True
            visited.add(n)
            queue += n.adj
        return False

def test_run():
    g = DiGraph()
    g.connect(1,2)
    g.connect(1,3)
    g.connect(2,3)
    g.connect(3,4)
    g.connect(4,5)
    g.connect(4,6)
    g.connect(5,6)
    print g.is_connected(1, 5)
