import numpy as np

#fh = open("input12-1.dat")
fh = open("test2.dat")

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

num = 0
for row in rows:
    print("----------------")
    print(row.strip("\n"))
    data, groupstr = row.split(" ")
    groups = [int(x) for x in groupstr.strip("\n").split(",")]

    tmp = list(data)
    print(tmp)
    qidxs = np.where(np.array(tmp)=="?")[0]
    print(qidxs)
    
    # Wildly inefficient, but good enough for this part
    new_ways = 0
    for combo in range(2**len(qidxs)):
        tmp2 = tmp.copy()
        bits = f"{combo:030b}"
        # print(bits)
        # print(bits[-len(qidxs):])
        for i, j in enumerate(bits[-len(qidxs):]):
            #print(i,j)
            c = "." if j=='0' else "#"
            tmp2[qidxs[i]] = c
        new_ways += validate(tmp2, groups)
        if new_ways > 0:
            print(tmp2, groups, new_ways)
        num += new_ways

print(num)