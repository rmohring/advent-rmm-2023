import pandas as pd
import numpy as np

fh = open("input9-1.dat")
# fh = open("test.dat")

lines = fh.readlines()
rows = [x.strip("\n").split(" ") for x in lines]
arrays = []
for row in rows:
    tmp = [int(x) for x in row]
    arrays.append(pd.Series(tmp))

shift = {}
offset = {}
next_val = {}
for idx, arr in enumerate(arrays):
    offset[idx] = 0
    tmp = arr.copy()
    for j in range(100):
        # print(idx, j)
        tmp = tmp.diff()
        offset[idx] += tmp.to_list()[-1]
        if np.all(tmp.fillna(0) == 0):
            shift[idx] = j
            next_val[idx] = arr.to_list()[-1] + offset[idx]
            break

print(next_val)
print(sum(next_val.values()))
