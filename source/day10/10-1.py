fh = open("input10-1.dat")
# fh = open("test.dat")

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

for i in range(1, 100000):
    pos = tuple_add(pos, step)
    cell = cells[pos[0]][pos[1]]
    tracker.append((i, pos, cell))
    if cell == "S":
        print("BACK TO S")
        break
    step_type = nav[cell]
    step = step_type[from_dir[step]]

print(i, "Answer: ", int(i / 2))
