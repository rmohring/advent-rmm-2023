import sys
import datetime

fh = open("input5-1.dat", "r")

start_seed = int(sys.argv[1])

level = {}
MAXLEVEL = 8

lines = fh.readlines()
for idx,line in enumerate(lines):
    if idx==0:  #seeds
        seeds = line.strip().split(':')[1].split()
        seeds = [int(x) for x in seeds]
    if line.startswith('seed-to-soil map:'):
        level[1] = idx
    if line.startswith('soil-to-fertilizer map:'):
        level[2] = idx
    if line.startswith('fertilizer-to-water map:'):
        level[3] = idx
    if line.startswith('water-to-light map:'):
        level[4] = idx
    if line.startswith('light-to-temperature map:'):
        level[5] = idx
    if line.startswith('temperature-to-humidity map:'):
        level[6] = idx
    if line.startswith('humidity-to-location map:'):
        level[7] = idx

level[MAXLEVEL] = len(lines)+1

my_map = {}

def fill_map(start_idx, end_idx):
    retval = []
    for i in range(start_idx+1, end_idx-1):
        line = lines[i].split()
        source_min = int(line[1])
        source_max = int(line[1])+int(line[2])
        offset = int(line[0])-int(line[1])
        retval.append( (source_min, source_max, offset))
    return sorted(retval)

for i in range(1, MAXLEVEL):
    my_map[i] = fill_map(level[i], level[i+1])

def traverse(source_val, transform_map):
    retval = source_val
    for (smin, smax, offset) in transform_map:
        if source_val>=smin and source_val<=smax:
            retval = source_val + offset
    return retval

def get_nowtime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")

hmin = 999999999999999999999999

# So, it's too many seeds to do serially, so this is a
# way to do each range in a separate executable
# by slicing the full list of seeds down to a single 
# range pair
print(start_seed)
seeds = seeds[start_seed*2:(start_seed*2)+2]
print(f"Clipping to {start_seed}:{seeds}")

# I need to store the output somewhere now because it won't be on screen
outfile = open(f"outfile_{start_seed}.txt","w",1)
outfile.write(f"{get_nowtime()}\n")

for i in range(0, len(seeds), 2):
    print(i, seeds[i], seeds[i+1])
    for j in range(seeds[i+1]):
        seed = seeds[i]+j
        b = traverse(seed, my_map[1])
        c = traverse(b, my_map[2])
        d = traverse(c, my_map[3])
        e = traverse(d, my_map[4])
        f = traverse(e, my_map[5])
        g = traverse(f, my_map[6])
        h = traverse(g, my_map[7])
        if j%500000==0:
             outfile.write(f"Iteration: {j} Left: {seeds[i+1]-j}\n")
        #     print(f"Iteration: {j} Left: {seeds[i+1]-j}")
        if h < hmin:
            hmin = h
        #    print(h)

outfile.write(f"{hmin}, from working {start_seed}\n")
outfile.write(f"{get_nowtime()}\n")
outfile.close()
