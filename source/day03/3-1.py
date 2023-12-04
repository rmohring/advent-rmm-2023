fh = open("input3-1.dat", "r")

grid = []
nums = []

for (rownum, raw_row) in enumerate(fh.readlines()):  
    row = list(raw_row.strip("\n"))
    grid.append(row)    
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
                print(rownum, numstr, raw_row.strip("\n"))
                numstr = ""
                is_in_a_num = False
    if is_in_a_num:
        nums.append( (rownum, start_idx, numstr))
        print(numstr, raw_row.strip("\n"))
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
                print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'rowbefore')
                return int(numstr)
                
    # Same row
    if start_idx > 0:
        cell = grid[rownum][prev_idx]
        if is_cell_special_char(cell):
            print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'charbefore')            
            return int(numstr)

    if start_idx+len(numstr) < NUMCOLS:
        cell = grid[rownum][next_idx]
        if is_cell_special_char(cell):
            print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'charafter')            
            return int(numstr)

    # Row after
    if rownum < NUMROWS:
        next_rownum = rownum + 1
        for idx in range(prev_idx, next_idx+1):
            cell = grid[next_rownum][idx]
            if is_cell_special_char(cell):
                print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'rowafter')            
                return int(numstr)

    print(rownum, numstr, start_idx, prev_idx, next_idx, len(numstr), 'NO!!!')                        
    return 0

sum = 0
MINROW, MAXROW = 0,4
for (rownum, start_idx, numstr) in nums:
    # if rownum<MINROW or rownum>MAXROW:
    #     continue
    val = get_part_num(rownum, start_idx, numstr)
    sum += val
    print(rownum, start_idx, numstr, val)

print(f"{NUMROWS, NUMCOLS}...Total is: {sum}")


            

            