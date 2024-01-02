import sys
#sys.path.append('c:/Users/rmohring/code/rmm/advent-rmm-2023')
sys.path.append('/home/rmohring/code/rmm/advent-rmm-2023')

import numpy as np
from collections import Counter
from util.grid import Gridder

fh = open("input23-1.dat")
#fh = open("test.dat")

lines = fh.readlines()
lines = [x.strip("\n") for x in lines]

g = Gridder()
for line in lines:
    g.addrow(line)
g.done_building()

nav = {  
    "U": (-1,0),
    "D": (1,0),
    "R": (0,1),
    "L": (0,-1),
}

def tupleadd(a,b):
    return (a[0]+b[0], a[1]+b[1])

maze = Gridder(g)

def get_options(history):
    # Look around, round
    pos  = history[-1]
    options = []
    for n, (vr,vc) in nav.items():
        new = tupleadd((pos[0],pos[1]),(vr,vc))
        if new[0]<0 or (new in history) or new[0]>maze.nrows-1:
            continue
        next_tile = g.val(new)
        if next_tile in [".",">","<","^","v"]:
            valid = True
            if ( (n=="U" and next_tile=="v")
                or (n=="D" and next_tile=="^")
                or (n=="R" and next_tile=="<")
                or (n=="L" and next_tile==">") ):
                valid=False
            if valid:
                options.append(new)
    return options


# everytime you hit multiple options
#    remember the number of steps so far and touched coords

history = [[(0,1)]]
solutions = []

for step in range(1,10000):
    newpaths = []
    for i,h in enumerate(history):
        options = get_options(h)
        # if i == 0:
        #     print(step, options)
        for o in options:
            if o[0]==maze.nrows-1:
                solutions.append(h + [o])
            else:
                newpaths.append(h + [o])
    history = newpaths.copy()

for s in solutions:
    print(len(s)-1)