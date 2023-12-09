import numpy as np

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

starting_locs = [x for x in locs.keys() if x.endswith("A")]
ending_locs = [x for x in locs.keys() if x.endswith("Z")]

ends = {}
debug = {}

# starting_locs = ["AAA"]
for key in starting_locs:
    done = False
    steps = 0
    debug[key] = []
    ends[key] = []
    this_loc = key
    while not done:
        for iii, turn in enumerate(dirs):
            steps += 1
            debug[key].append((steps, iii, this_loc))
            next_loc = locs[this_loc][turn]
            if next_loc in ending_locs:
                ends[key].append(steps)
                if len(ends[key]) > 3:
                    print(key, steps)
                    done = True
                    break
            this_loc = next_loc

first_z = {}
offsets = {}
for key in starting_locs:
    first_z[key] = ends[key][0]
    offsets[key] = ends[key][1] - ends[key][0]

print(first_z)
print(offsets)

answer = np.lcm.reduce(list(offsets.values()))
print("Answer", answer)

for key in starting_locs:
    print(key, first_z[key], offsets[key])
    print((answer - first_z[key]) / offsets[key])
