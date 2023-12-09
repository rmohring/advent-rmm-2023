from collections import Counter

fh = open("input8-1.dat", "r")
# fh = open("test.dat", "r")

lines = fh.readlines()

dirs = lines[0].strip("\n").replace("R", "1").replace("L", "0")
dirs = [int(x) for x in list(dirs)]

locs = {}
for line in lines[2:]:
    (loc, b) = line.strip("\n").split("=")
    loc = loc.replace(" ", "")
    b = b.replace("(", "").replace(")", "")
    left, right = b.split(", ")
    left = left.replace(" ", "")
    right = right.replace(" ", "")
    locs[loc] = [left, right]

this_loc = "AAA"
done = False
steps = 0
while not done:
    for turn in dirs:
        steps += 1
        next_loc = locs[this_loc][turn]
        if next_loc == "ZZZ":
            done = True
            break
        else:
            this_loc = next_loc

print(steps)
