import sys
#sys.path.append('c:/Users/rmohring/code/rmm/advent-rmm-2023')
sys.path.append('/home/rmohring/code/rmm/advent-rmm-2023')

import numpy as np
import copy
from collections import Counter

#fh = open("input25-1.dat")
fh = open("test.dat")
#fh = open("test2.dat")

lines = fh.readlines()
lines = [x.strip("\n") for x in lines]

class Graph:
    def __init__(self):
        self.edges = set()
        self.nodes = {}

    def process_str(self, initstr):
        spl = initstr.split(": ")
        source = spl[0]
        ends = spl[1].split(" ")
        for e in ends:
            self.add_edge(source, e)

    def add_edge(self, a, b):
        self.edges.add( (a,b) )

    def finalize(self):
        for (a,b) in self.edges:
            if a not in self.nodes:
                self.nodes[a] = set()
            self.nodes[a].add(b)
            if b not in self.nodes:
                self.nodes[b] = set()
            self.nodes[b].add(a)


def traverse(this_node, start_node, seen=None, first_step=False):
    print(start_node, this_node, "seen:", seen)
    local_seen =seen.copy()

    # Go to node and pick a new option
    next_options = [next_node for next_node in g.nodes[this_node] if next_node not in seen]
    print("... NEXT OPTIONS", next_options)
    if start_node in next_options and not first_step:
        return True
    for next_node in next_options:
        if next_node == start_node:
            continue
        print(next_node)
        local_seen.add(next_node)
        not_a_bridge = traverse(next_node, start_node, local_seen)
        if not_a_bridge:
            print("TRUETRUE")
            return True
    print("BLAH!")
    return False  
    
g = Graph()
for line in lines:
    g.process_str(line)

g.finalize()

bridges = []
# for n, ends in g.nodes.items():
#     for chk in ends:

if True:
    if True:
        n = 'hfx'
        chk = 'pzl'
        print(f"Working start node: {n}; first edge {n}-{chk}")
        # Go to chk
        # Pick a new end that isn't one we've stepped on
        # Run through all permutations... 
        # if none end on "n" without hitting "chk", it's a bridge edge
        seen = set([chk])
        not_a_bridge = traverse(chk, n, seen, first_step=True)
        #print(n, chk, not_a_bridge)
        if not not_a_bridge:
            bridges.append( (n, chk) )


