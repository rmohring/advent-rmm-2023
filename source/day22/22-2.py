import sys
#sys.path.append('c:/Users/rmohring/code/rmm/advent-rmm-2023')
sys.path.append('/home/rmohring/code/rmm/advent-rmm-2023')

import numpy as np
import copy
from collections import Counter

fh = open("input22-1.dat")
#fh = open("test.dat")
#fh = open("test2.dat")

lines = fh.readlines()
lines = [x.strip("\n") for x in lines]

class Brick:
    def __init__(self, initstr=None, cubes=None, name=None, oldname=None) -> None:
        self.name = name
        if self.name is None:
            self.name = "NoName"

        self.oldname = oldname
        if self.oldname is None:
            self.oldname = self.name

        if initstr is not None:
            end1, end2 = initstr.split("~")
            self.end1 = [int(x) for x in end1.split(",")]
            self.end2 = [int(x) for x in end2.split(",")]
            print(self.end1, self.end2)
            xlen = (self.end2[0] - self.end1[0])
            ylen = (self.end2[1] - self.end1[1])
            zlen = (self.end2[2] - self.end1[2])
               
            self.cubes = []
            for i in range(xlen+1):
                for j in range(ylen+1):
                    for k in range(zlen+1):
                        self.cubes.append( (i+self.end1[0], j+self.end1[1], k+self.end1[2]))
        elif cubes is not None:
            self.cubes = cubes

    @property
    def nbricks(self):
        return len(self.cubes)
    
    @property
    def min_z_level(self):
        return min( (z for (x,y,z) in self.cubes) )
    
    def __repr__(self):
        return self.__str__()
    
    def __str__(self):
        return f"Brick {self.name:3s} : {self.cubes}"



def fall_by_one(blk):
    new_cubes = []
    for c in blk.cubes:
        new_cubes.append( (c[0],c[1],c[2]-1) )

    return Brick(cubes=new_cubes, name=blk.name)

def valid_fall(newblk, stk):
    # Check the floor first
    for c in newblk.cubes:
        if c[2]<1:
            return False
        
    # Then find collisions
    for n, blk in stk.items():
        if blk.name == newblk.name:
            continue
        if len(set(newblk.cubes).intersection(set(blk.cubes))) > 0:
            # print("XX:", new_blk.cubes, blk.cubes)
            # print("X2:", set(new_blk.cubes).intersection(set(blk.cubes)))
            return False

    return True

def copy_stack(stk):
    newstack = {}
    for bnum, brk in stk.items():
        newstack[bnum] = Brick(cubes=brk.cubes, name=brk.name)
    return newstack

def apply_gravity(stk):
    stkcopy = copy_stack(stk)
    for (i, (bnum, brk)) in enumerate(stk.items()):
        done = False
        tmpbrk = Brick(cubes=brk.cubes, name=brk.name)
        while not done:
            tmpbrk = fall_by_one(tmpbrk)
            if valid_fall(tmpbrk, stkcopy):
                stkcopy[bnum] = Brick(cubes=tmpbrk.cubes, name=tmpbrk.name)
            else:
                #print("NO!", i,bnum,brk,tmpbrk)
                done = True
    return stkcopy

# def check_disintegration(self, bnum, stk):
#     tmp = copy.deepcopy(stk)
#     del tmp[bnum]
#     new = apply_gravity(tmp)

def stacks_are_equal(s1, s2):
    equal = True
    for name, blk in s1.items():
        if set(blk.cubes) != set(s2[name].cubes):
            equal = False

    for name, blk in s2.items():
        if set(blk.cubes) != set(s1[name].cubes):
            equal = False

    return equal

def get_num_fallen_stacks(s1, s2):
    fallen = 0
    for name, blk in s1.items():
        if set(blk.cubes) != set(s2[name].cubes):
            fallen += 1
    return fallen

presort_stack = {}
for i,line in enumerate(lines):
    presort_stack[i] = Brick(initstr=line, name=str(i))

# Apparently I need to sort the stack first. "Snapshot", my butt.
sorter = []
for bnum, brk in presort_stack.items():
    sorter.append( (brk.min_z_level, bnum) )
sorter = sorted(sorter)

stack = {}
print("Sorting...")
for i, (level, bnum) in enumerate(sorter):
    tmp = presort_stack[bnum]
    stack[i] = Brick(cubes=tmp.cubes, name=str(i), oldname=tmp.name)

print("Applying gravity, first time...")
stack = apply_gravity(stack)

the_fallen = []
for i in stack:
    print(f"Working {i} of {len(stack)}...")
    tmp = copy_stack(stack)
    del tmp[i]
    chk = apply_gravity(tmp)
    the_fallen.append(get_num_fallen_stacks(tmp, chk))
    
print("Safe bricks: ", len( [x for x in the_fallen if x==0] ))
print("Answer:", sum(the_fallen))