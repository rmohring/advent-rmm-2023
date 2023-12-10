import pandas as pd
import numpy as np

fh = open("input10-1.dat")
# fh = open("test2.dat")

lines = fh.readlines()
cells = [x.strip("\n") for x in lines]
# From N,S,W,E (U,D,L,R)
nav = {  # (Row (UD), Col (LR))
    "-": ((0, 0), (0, 0), (0, 1), (0, -1)),
    "|": ((1, 0), (-1, 0), (0, 0), (0, 0)),
    "L": ((0, 1), (0, 0), (0, 0), (-1, 0)),
    "F": ((0, 0), (0, 1), (0, 0), (1, 0)),
    "7": ((0, 0), (0, -1), (1, 0), (0, 0)),
    "J": ((0, -1), (0, 0), (-1, 0), (0, 0)),
}
from_dir = {
    (1, 0): 0,  # from U
    (-1, 0): 1,  # from D
    (0, 1): 2,  # from L
    (0, -1): 3,  # from R
}


def tuple_add(a, b):
    return tuple(map(lambda i, j: i + j, a, b))


start_row = -1
for idx_row, row in enumerate(cells):
    for idx_col in range(len(row)):
        if cells[idx_row][idx_col] == "S":
            start_row = idx_row
            start_col = idx_col
            break
    if start_row > -1:
        break

pos = (start_row, start_col)
print(pos)

tracker = [(0, pos, cells[pos[0]][pos[1]])]
step = (0, -1)
# step = (1, 0)
for i in range(1, 100000):
    pos = tuple_add(pos, step)
    cell = cells[pos[0]][pos[1]]
    tracker.append((i, pos, cell))
    if cell == "S":
        print("BACK TO S")
        break
    step_type = nav[cell]
    step = step_type[from_dir[step]]

print(i, i / 2)

# Clean out all the spaces and junk pipes
newcells = []
for i in range(len(cells)):
    newcells.append([" " for j in range(len(cells[0]))])

for (i, (r, c), sym) in tracker:
    newcells[r][c] = sym

# outfh = open("input10-2.dat", "w")
# for i in range(len(cells)):
#     outfh.write("".join(newcells[i]))
#     outfh.write("\n")
# outfh.close()

# For every cell,
# Count crossings from the left to the edge,
# Weighting them as:  | = 1; (L,7) = 0.5; (F,J) = -0.5; - = 0
# If you cross an odd number, it's in the middle

total = 0
for i, row in enumerate(newcells):
    edge_ctr = 0
    inside_ctr = 0
    for j, cell in enumerate(row):
        if cell in ["|"]:
            edge_ctr += 1
        elif cell in ["L", "7"]:
            edge_ctr += 0.5
        elif cell in ["F", "J"]:
            edge_ctr += -0.5
        elif cell == " ":
            if edge_ctr % 2 == 1:
                # print(i, j, edge_ctr)
                inside_ctr += 1
    print(f"{i} edges {edge_ctr} inside {inside_ctr}")
    total += inside_ctr

print(total)
