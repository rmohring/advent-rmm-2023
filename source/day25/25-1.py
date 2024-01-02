import sys
#sys.path.append('c:/Users/rmohring/code/rmm/advent-rmm-2023')
sys.path.append('/home/rmohring/code/rmm/advent-rmm-2023')

import numpy as np
import copy
from collections import Counter

fh = open("input25-1.dat")
#fh = open("test.dat")
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


results = {}

def traverse(this_node, start_node, seen=None, level=0):
    level += 1
    local_seen = seen.copy()

    #print(start_node, this_node, "seen:", seen)
    # Go to node and pick a new option
    next_options = [next_node for next_node in g.nodes[this_node] if next_node not in seen]
    #print("... NEXT OPTIONS", next_options)
    for next_node in next_options:
        #print(next_node)
        results[(start_node, next_node)] = min(results.get((start_node, next_node),999999), level)
        local_seen.add(next_node)
        
        traverse(next_node, start_node, seen=local_seen, level=level)
    return
    
g = Graph()
for line in lines:
    g.process_str(line)

g.finalize()


for n in g.nodes:
    print(f"Working start node: {n}...")
    seen = set([n])
    traverse(n, n, seen, level=0)

print("Calculating eccentricities...")
eccentricity = {}
for n in g.nodes:
    print(n)
    eccentricity[n] = max([ecc for (a,b),ecc in results.items() if a==n])

print("Calculating edge ecc sums...")
ecc_sum = {}
for (n1,n2) in g.edges:
    print(n1,n2)
    ecc_sum[(n1,n2)] = eccentricity[n1] + eccentricity[n2]


# Eccentricity --> E
# Can reach EVERY other nodex in "E" steps or fewer
# Lowest E nodes are the candidates as bridge nodes to snip?

