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

starting_locs = [x for x in locs.keys() if x.endswith("A")]
ending_locs = [x for x in locs.keys() if x.endswith("Z")]

print(starting_locs)
print(ending_locs)

this_loc = {}
ends = {}
for key in starting_locs:
    this_loc[key] = key
    ends[key] = []

done = False
# keys_to_check = starting_locs  # ["AAA", "VXA"]
keys_to_check = starting_locs  # ["AAA", "JHA", "PXA"]

steps = 0
while not done:
    for turn in dirs:
        steps += 1
        done = True

        for key in keys_to_check:
            next_loc = locs[this_loc[key]][turn]

            if next_loc in ending_locs:
                ends[key].append(steps)
                print(steps, key, this_loc[key], next_loc)
            done &= next_loc in ending_locs

            this_loc[key] = next_loc

        if done:
            print(f"DONE: steps = {steps}")
            for k in keys_to_check:
                print(this_loc[k])
            break

        if steps > 100000:
            print("=================")
            done = True
            break

        # if zs == len(starting_locs):
        #    print(f"DONE: steps = {steps}")
        #    done = True
        #    break

print(steps)
for k in keys_to_check:
    print(k)
    print(ends[k])
    print(ends[k][0], ends[k][2] - ends[k][1])
