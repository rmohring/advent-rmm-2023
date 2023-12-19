fh = open("input15-1.dat")

rows = fh.readlines()[0].strip("\n")
#rows = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

groups = rows.split(",")

instructions = []

for g in groups:
    curr = 0
    if "=" in g:
        (label, fl) = g.split("=")
    else:
        (label, fl) = (g[:-1], -1)    
    gvals = [ord(x) for x in label]
    for a in gvals:
        curr = ((curr + a) * 17) % 256
    instructions.append( (curr, label, fl) )

# Yay, can do this with regular dictionaries these days because they are ordered
boxes = [ {} for i in range(256)]

for (nbox, label, fl) in instructions:
    if fl != -1:
        boxes[nbox][label] = int(fl)
    elif label in boxes[nbox]:
        del(boxes[nbox][label]) 

tot = 0
for i, box in enumerate(boxes):
    focus_power = 0
    for j, (k,fl) in enumerate(box.items()):
        focus_power += (i+1) * (j+1) * fl
    tot += focus_power
print(tot)
