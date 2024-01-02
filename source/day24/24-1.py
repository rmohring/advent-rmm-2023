import sys
#sys.path.append('c:/Users/rmohring/code/rmm/advent-rmm-2023')
sys.path.append('/home/rmohring/code/rmm/advent-rmm-2023')

import numpy as np
import copy
from collections import Counter

fh = open("input24-1.dat")
#fh = open("test.dat")
#fh = open("test2.dat")

#X_RANGE = (7, 27)
#Y_RANGE = (7, 27)
X_RANGE = (200000000000000, 400000000000000)
Y_RANGE = (200000000000000, 400000000000000)

lines = fh.readlines()
lines = [x.strip("\n") for x in lines]

class Hailstone:
    def __init__(self, initstr):
        coords, velocities = initstr.split("@")
        (self.x0,self.y0,self.z0) = tuple([int(qq) for qq in coords.replace(" ","").split(",")])
        (self.vx0,self.vy0,self.vz0) = tuple([int(qq) for qq in velocities.replace(" ","").split(",")])

    def position(self, t):
        xpos = self.x0 + self.vx0*t
        ypos = self.x0 + self.vx0*t
        zpos = self.x0 + self.vx0*t
        return (xpos, ypos, zpos)
    
    def get_time_at_xy(self, pos_tup):
        if pos_tup is None:
            return None
        return (pos_tup[0]-self.x0)/self.vx0
    
    @property
    def yx_slope(self):
        return self.vy0/self.vx0
    
    @property
    def yx_y_intercept(self):
        return self.y0 - self.yx_slope*self.x0

    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self) -> str:
        return f"({self.x0:15d},{self.y0:15d},{self.z0:15d}) with v: ({self.vx0:5d},{self.vy0:5d},{self.vz0:5d})"

hail = []
for line in lines:
    hail.append(Hailstone(line))

def get_yx_intersection(h1, h2):
    if h1.yx_slope == h2.yx_slope:
        return None
    xpos = (h2.yx_y_intercept-h1.yx_y_intercept)/(h1.yx_slope - h2.yx_slope)
    ypos = h1.yx_slope * xpos + h1.yx_y_intercept
    return (xpos, ypos)
            

def is_between(val, range_tup):
    return (val>=range_tup[0]) and (val<=range_tup[1])

total = 0
for i in range(len(hail)):
    for j in range(i+1, len(hail)):
        pos = get_yx_intersection(hail[i], hail[j])
        t_i = hail[i].get_time_at_xy(pos)
        t_j = hail[j].get_time_at_xy(pos)
        print(i,j, pos, t_i, t_j)
        if pos is not None:
            if t_i>0 and t_j>0 and is_between(pos[0], X_RANGE) and is_between(pos[1], Y_RANGE):
                total += 1

print(total)
# 4200 was too low
#21148 was too high

