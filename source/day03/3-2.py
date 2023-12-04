fh = open("input3-1.dat", "r")
#fh = open("test.dat", "r")

grid = []
nums = []

lines = fh.readlines()

# Strip out everything but numbers, periods, and stars
for raw_row in lines:  
    row = []
    for c in list(raw_row.strip("\n")):
        if (c.isnumeric() or c=='.' or c=='*'):
            row.append(c)
        else:
            row.append('.')
    grid.append(row)    

for (rownum, row) in enumerate(grid):  
    is_in_a_num = False
    numstr = ""
    for idx,c in enumerate(row):
        if c.isnumeric():
            if not is_in_a_num:
                is_in_a_num = True
                start_idx = idx
            numstr += c
        else:
            if is_in_a_num:
                nums.append( (rownum, start_idx, numstr))
                # print(rownum, numstr, raw_row.strip("\n"))
                numstr = ""
                is_in_a_num = False               
    if is_in_a_num:
        nums.append( (rownum, start_idx, numstr))
        # print(numstr, raw_row.strip("\n"))
        numstr = ""
        is_in_a_num = False

NUMCOLS = len(row)  # Assuming a rectangle
NUMROWS = rownum
part_numbers = []

def is_cell_special_char(cell):
    return (not cell.isnumeric()) and (not cell==".")

def get_part_num(rownum, start_idx, numstr):
    prev_idx = max(start_idx-1, 0)
    next_idx = min(start_idx+len(numstr), NUMCOLS-1)

    # Row before
    if rownum > 0:
        prev_rownum = rownum - 1
        for idx in range(prev_idx, next_idx+1):
            cell = grid[prev_rownum][idx]
            if is_cell_special_char(cell):
                # print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'rowbefore')
                return ((prev_rownum, idx), int(numstr))
                
    # Same row
    if start_idx > 0:
        cell = grid[rownum][prev_idx]
        if is_cell_special_char(cell):
            # print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'charbefore')            
            return ((rownum,prev_idx), int(numstr))

    if start_idx+len(numstr) < NUMCOLS:
        cell = grid[rownum][next_idx]
        if is_cell_special_char(cell):
            # print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'charafter')            
            return ((rownum, next_idx), int(numstr))

    # Row after
    if rownum < NUMROWS:
        next_rownum = rownum + 1
        for idx in range(prev_idx, next_idx+1):
            cell = grid[next_rownum][idx]
            if is_cell_special_char(cell):
                # print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'rowafter')            
                return ((next_rownum, idx), int(numstr))

    print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'NO!!!')                        
    return ((-1,-1),0)

gear_candidates = {}
for (rownum, start_idx, numstr) in nums:
    (star_location, val) = get_part_num(rownum, start_idx, numstr)
    if star_location not in gear_candidates:
        gear_candidates[star_location] = [val]
    else:
        gear_candidates[star_location].append(val)
sum = 0
for (gloc, vals) in gear_candidates.items():
    if len(vals)==2:
        print(gloc, vals)
        sum += vals[0]*vals[1]

print(f"{NUMROWS, NUMCOLS}...Total is: {sum}")


            

            