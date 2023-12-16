fh = open("input15-1.dat")

rows = fh.readlines()[0].strip("\n")
#rows = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

groups = rows.split(",")
gvals = [[ord(x) for x in grp] for grp in groups]

tot = 0
for g in gvals:
    curr = 0
    for a in g:
        curr = ((curr + a) * 17) % 256
    tot += curr
    
print(tot)