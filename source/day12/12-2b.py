import numpy as np

fh = open("input12-1.dat")
#fh = open("test.dat")

rows = fh.readlines()

DEBUG = False
def dprint(*x):
    if DEBUG:
        print(*x)

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
    dprint(idx, row.strip("\n"))
    data, groupstr = row.split(" ")
    groups = [int(x) for x in groupstr.strip("\n").split(",")]

    dprint(data, groups)
    data = "?".join([data]*5)
    groups = groups*5
    print(data, groups)
    data2 = data.split(".")
    dprint(data2)
    data3 = [x for x in data2 if x!=""]
    dprint(data3)

    dprint(f'Num ?: {data.count("?")}; Num #: {data.count("#")}; Sum groups: {sum(groups)}')
    # How many more # do we need?
    need = sum(groups)-data.count("#")
    print("*****", data.count("?"), need)
    # for substr in data3:
    #     if "?" in substr:
    #         print(substr, searcher(substr))
              
print(num)


def chomp(pattern, size):
    if "?" not in pattern:
        return []

    patt = list(pattern)
    done = False
    start = 0
    while not done:
        tmp = patt.copy()
        for i in range(start):
            if tmp[i]=="?":
                tmp[i] = "."
        if start+size > len(tmp):
            return []
        for j in range(start, start+size):
            if tmp[i]=="#":
                pass
            elif tmp[i] == "?"
                tmp[i] = "#"
        
        if start+size < len(tmp):
            if tmp[start+size+1]=="#":
                return []



# groups = [1,2,3,4]
# substr = "???#...##????#????"
# strlist = ["???#","##????#????"]

# # try to fit first group in first slot
# # shove "#." in beginning
# test = ["#.?#","##????#????"]
# # Resplit and flatten, and drop first
# strlist = ["#","?#","##????#????"]
# strlist = ["?#","##????#????"]
# groups = [2,3,4]

# # try to fit first group in first slot
# # shove "#." in beginning
# test = ["#.?#","##????#????"]
# # Resplit and flatten, and drop first
# strlist = ["#","?#","##????#????"]
# strlist = ["?#","##????#????"]
# groups = [2,3,4]

# 1 = "?" or "#"
# 2 = "??" or "?#" or "#?"
# 3 = "???]", or "????" ?##", "#??"

# group = 2
# start from beginning of string
# if starts with "#"... go until "?#" or end







