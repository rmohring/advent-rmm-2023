import numpy as np
import copy

fh = open("input18-1.dat")
#fh = open("test.dat")

lines = fh.readlines()

instructions = []
for line in lines:
    direction, num, color = line.strip().split()
    color = color.replace("(","").replace(")","")
    instructions.append( (direction, int(num), color))

nav = {  
    "U": (-1,0),
    "D": (1,0),
    "R": (0,1),
    "L": (0,-1),
}

def tupleadd(a,b):
    return (a[0]+b[0], a[1]+b[1])

pos = (0,0)
# cells = set()
# cells.add(pos)
cells = []
cells.append(pos)
for direction, count, color in instructions:
    for i in range(count):
        pos = tupleadd(pos, nav[direction])
        #cells.add(pos)
        cells.append(pos)


nrows = max((x[0] for x in cells)) - min((x[0] for x in cells)) + 1
ncols = max((x[1] for x in cells)) - min((x[1] for x in cells)) + 1
offset_rows = min((x[0] for x in cells)) 
offset_cols = min((x[1] for x in cells))

grid = []
for i in range(nrows):
    grid.append( ["."]*ncols )

for i,j in cells:
    grid[i-offset_rows][j-offset_cols] = "#"

for i in range(nrows):
    for j in range(ncols):
        print(grid[i][j], end="")
    print()


# ctr = 0
# for i, row in enumerate(grid):
#     if i==0:
#         continue
#     for j, c in enumerate(row):
#         if j==0:
#             continue
#         if (filled[i][j-1] == "#") and (filled[i-1][j] == "#"):
#             filled[i][j] = "#"

# I know it's a loop, and from looking at it, I know that (1,1) is inside



tmp = copy.deepcopy(grid)
tmp[1-offset_rows][1-offset_cols] = "x"

found = True
ctr = 0
while found:
    ctr += 1
    if ctr % 10==0:
        print(ctr)
    found = False
    filled = copy.deepcopy(tmp)
    for i, row in enumerate(filled):
        if (i==0) or (i==len(filled)):
            continue
        #print(i, row, np.where(np.array(row)=='x'))
        for j in np.where(np.array(row)=='x')[0]:
            if (j==0) or (j==len(row)):
                continue
            if tmp[i][j-1] == ".":
                tmp[i][j-1] = "x"
                found = True
            if tmp[i][j+1] == ".":
                tmp[i][j+1] = "x"
                found = True
            if tmp[i-1][j] == ".":
                tmp[i-1][j] = "x"
                found = True
            if tmp[i+1][j] == ".":
                tmp[i+1][j] = "x"
                found = True

ctr = 0
for i in range(nrows):
    for j in range(ncols):
        print(filled[i][j], end="")
        ctr += (filled[i][j] in ["#","x"])
    print()

print("Answer:", ctr)
        
