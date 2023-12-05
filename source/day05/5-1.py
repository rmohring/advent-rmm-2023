fh = open("input5-1.dat", "r")
#fh = open("test.dat", "r")
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

locations = []
for seed in seeds:
    b = traverse(seed, my_map[1])
    c = traverse(b, my_map[2])
    d = traverse(c, my_map[3])
    e = traverse(d, my_map[4])
    f = traverse(e, my_map[5])
    g = traverse(f, my_map[6])
    h = traverse(g, my_map[7])
    locations.append( (h, seed) )

for loc in sorted(locations):
    print(loc)