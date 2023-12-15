import numpy as np

fh = open("input13-1.dat")
#fh = open("test.dat")

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

def get_mirror_val(image, mult=None):
    is_mirror = False
    this_val = []

    for rnum in range(len(image)-1):
        dprint(rnum, image[rnum] == image[rnum+1])
        if image[rnum] == image[rnum+1]:
            is_mirror = True
            for test_rnum in range(rnum,-1,-1):
                mirror_rnum = 2*rnum + 1 - test_rnum
                dprint("........",test_rnum, mirror_rnum)
                if mirror_rnum < len(image):
                    is_mirror &= (image[test_rnum] == image[mirror_rnum])
            if is_mirror:
                this_val.append(mult * (rnum+1))

    return this_val

tot = 0
for ctr, image in enumerate(images):
    print(f"Working {ctr}...")
    this_val = get_mirror_val(image, mult=100)
    print(this_val)
    if len(this_val) == 0:
        this_val = get_mirror_val(transpose(image), mult=1)

    tot += this_val[0]
    print(ctr, this_val[0])

print("Answer:", tot)