import sys
#sys.path.append('c:/Users/rmohring/code/rmm/advent-rmm-2023')
sys.path.append('/home/rmohring/code/rmm/advent-rmm-2023')

import numpy as np
from collections import Counter
from util.grid import Gridder

fh = open("input21-1.dat")
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

tmp = Gridder(g)
record = Gridder(g)

def get_coords_where(gridder, val):
    a = np.array(np.where(gridder.grid==val))
    return list(zip(a[0],a[1]))

start_pos = get_coords_where(g, "S")
tmp.grid[start_pos[0]] = "O"
record.grid[start_pos[0]] = "O"

#print(g.pretty(" "))

step = 1
TOT_STEPS = 64
while step <= TOT_STEPS:
    o_positions = get_coords_where(tmp, "O")
    possible_end_positions = []
    for o_pos in o_positions:
        tmp.grid[o_pos] = "."
        for d,v in nav.items():
            new_pos = tupleadd(o_pos, v)
            if tmp.grid[new_pos] == ".":
                possible_end_positions.append(new_pos)

    for p in possible_end_positions:
        tmp.grid[p] = "O"

    # print("==========================")
    # print(f"Step: {step}")
    # print(tmp.pretty(" "))
    step += 1

print("************")
print("Reachable plots:", len(get_coords_where(tmp, "O")))



        




