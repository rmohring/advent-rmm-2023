import numpy as np

#fh = open("input12-1.dat")
fh = open("test.dat")

rows = fh.readlines()

def validate(d, g):
    dstr = "".join(d)
    d2 = dstr.replace("."," ").split()
    if len(d2) != len(g):
        return 0
    val = True
    for a,b in zip(d2,g):
        val &= (len(a)==b)
    return int(val)  

def searcher(pattern):
    if "?" not in pattern:
        return []
    valid_subsets = []
    patt = list(pattern)
    qidxs = np.where(np.array(patt)=="?")[0]
    print(2**len(qidxs))
    for combo in range(2**len(qidxs)):
        tmp2 = patt.copy()
        bits = f"{combo:030b}"
        for i, j in enumerate(bits[-len(qidxs):]):
            c = "." if j=='0' else "#"
            tmp2[qidxs[i]] = c
        
        dstr = "".join(tmp2)
        d2 = dstr.replace("."," ").split()
        valid_subsets.append([len(x) for x in d2])
    
    return valid_subsets[1:]

num = 0
for idx,row in enumerate(rows):
    print(idx, row)
    data, groupstr = row.split(" ")
    groups = [int(x) for x in groupstr.strip("\n").split(",")]

    print(data, groups)
    data = "?".join([data]*5)
    groups = groups*5
    print(data, groups)
    data2 = data.split(".")
    print(data2)
    data3 = [x for x in data2 if x!=""]
    print(data3)

    for substr in data3:
        if "?" in substr:
            print(substr, searcher(substr))
              
print(num)