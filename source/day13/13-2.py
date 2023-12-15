import numpy as np
from copy import deepcopy

fh = open("input13-1.dat")
#fh = open("test.dat")
#fh = open("test000.dat")

rows = fh.readlines()
images = []
image = []
for row in rows:
    r = row.strip("\n")
    if r=="":
        images.append(image.copy())
        image = []
    else:
        image.append(list(r))

# Get the last one
images.append(image.copy())

def transpose(image):
    return np.array(image).T.tolist()

def print_image(image, T=False):
    if not T:
        for x in image:
            print(" ".join(x))
    else:
        for x in transpose(image):
            print(" ".join(x))   

DEBUG = False
def dprint(*x):
    if DEBUG:
        print(*x)

def compare_rows(row1, row2):
    diffs = [i for i, (a,b) in enumerate(zip(row1,row2)) if a!=b]
    return diffs

def get_mirror_val(img, mult=None):
    is_mirror = False
    this_val = []
    #print_image(img)
    for rnum in range(len(img)-1):
        print(rnum, img[rnum] == img[rnum+1])
        if img[rnum] == img[rnum+1]:
            is_mirror = True
            for test_rnum in range(rnum,-1,-1):
                mirror_rnum = 2*rnum + 1 - test_rnum
                print("........",test_rnum, mirror_rnum)
                if mirror_rnum < len(img):
                    print(img[test_rnum] == img[mirror_rnum])
                    is_mirror &= (img[test_rnum] == img[mirror_rnum])
            if is_mirror:
                this_val.append(mult * (rnum+1))

    return this_val

tot = 0
keepvals = []
for ctr, image in enumerate(images):
    print('==========================================')
    print(f"Working {ctr}...")
    print('==========================================')

    keep_val = 0
    this_val = []

    orig_val = get_mirror_val(image, mult=100)
    is_transpose = False
    if len(orig_val) == 0:
        orig_val = get_mirror_val(transpose(image), mult=1)
        is_transpose = True

    orig_val = orig_val[0]
    print("ORIGINAL: ", orig_val)

    # Normal, find off-by-ones
    obo = []
    for rnum in range(len(image)):
        for other_rnum in range(rnum+1, len(image)):
            diffs = compare_rows(image[rnum], image[other_rnum])
            if len(diffs)==1:
                obo.append( (rnum, other_rnum, diffs[0]) )
        
    if True or len(obo)>0:
        print_image(image)
        
    for (rnum, other_rnum, cnum) in obo:
        ## Try 'em all
        tmp = deepcopy(image)
        tmp[rnum][cnum] = tmp[other_rnum][cnum]
        print(f"TRYING: {rnum}-{other_rnum} col {cnum}")
        print_image(image)
        print('========')
        print_image(tmp)
        print('=============')
        this_val = get_mirror_val(tmp, mult=100)
        print("OBO: ", obo, this_val, orig_val)
        if this_val:
            success = False
            for x in this_val:
                if x!=orig_val:
                    success = True
            if success:
                break

    if orig_val in this_val:
        this_val.remove(orig_val)
        if this_val:
            keep_val = this_val[0]
    elif len(this_val)>0:
        keep_val = this_val[0]
    
    if keep_val==0:
        image_T = transpose(image).copy()
        obo = []
        for rnum in range(len(image_T)):
            for other_rnum in range(rnum+1, len(image_T)):
                diffs = compare_rows(image_T[rnum], image_T[other_rnum])
                if len(diffs)==1:
                    obo.append( (rnum, other_rnum, diffs[0]) )
        
        if True or len(obo)>0:
            print_image(image_T)

        for (rnum, other_rnum, cnum) in obo:
            ## Try 'em all
            tmp = deepcopy(image_T)
            tmp[rnum][cnum] = tmp[other_rnum][cnum]
            print("*****", rnum, other_rnum, cnum)
            print_image(tmp)

            this_val = get_mirror_val(tmp, mult=1)
            print("TOBO: ", obo, this_val, orig_val)
            if this_val:
                success = False
                for x in this_val:
                    if x!=orig_val:
                        success = True
                if success:
                    break

        if orig_val in this_val:
            this_val.remove(orig_val)
            if this_val:
                keep_val = this_val[0]
        elif len(this_val)>0:
            keep_val = this_val[0]

    tot += keep_val

    if keep_val == 0:
        keep_val = (keep_val, orig_val, is_transpose, len(image), len(image[0]))

    print("keeper = ", keep_val)
    keepvals.append(keep_val)
    # print(ctr, this_val[0])

for i,k in enumerate(keepvals):
    print(i, k)

print("Answer:", tot)

