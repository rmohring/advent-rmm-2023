import sys
#sys.path.append('c:/Users/rmohring/code/rmm/advent-rmm-2023')
sys.path.append('/home/rmohring/code/rmm/advent-rmm-2023')

import numpy as np
import math
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


def get_coords_where(gridder, val):
    a = np.array(np.where(gridder.grid==val))
    return list(zip(a[0],a[1]))

A_grid = Gridder(g)

for i in range(0, A_grid.nrows):
    for j in range(i % 2, A_grid.ncols, 2):
        if A_grid.grid[i,j] == ".":
            A_grid.grid[i,j] = "O"

B_grid = Gridder(g)
for i in range(0, B_grid.nrows):
    for j in range((i+1) % 2, B_grid.ncols, 2):
        if B_grid.grid[i,j] == ".":
            B_grid.grid[i,j] = "O"

print("************")
num_A_Os = len(get_coords_where(A_grid, "O"))
num_B_Os = len(get_coords_where(B_grid, "O"))
print("Number of Os in a full A grid:", num_A_Os)
print("Number of Os in a full B grid:", num_B_Os)

val = 26501365 // 131
print(f"Total grids: {val} x {val}")


# It's this kind of thing
# So it's a question of figuring out how many there
# are in a "full tile" (simple pattern, just
# deleting the "#" spots) then getting the 
# symmmetric remainders in the 4 directions

# In [74]: print(A_grid.pretty())                                      
# ...................O..............
# ......#...........O.O........###..
# ...#.##..........O.O.O........#...
# ...##.##.#......O.O.O.O....#..#.#.
# ...............O.O.O.O.O.....#.#..
# .....#........O.O.O.O.O.O.........
# ..#..#.......O.O.O.O#O.O.O........
# ........#...O.O.O#O.O.#.O.O...#...
# ..###..#...O.O.O.O#O#O.O.O.O....#.
# .....##...O.O.O#O.O.O.O.O.O.O.....

# When set to 10 steps
# The middle row is 11 Os: ..O.O.O.O.O.O.O.O.O.O.O..
#   extending to cell 11
# same thing vertically

# So, after 65 steps, the diamond covers the 131 across
# Then

