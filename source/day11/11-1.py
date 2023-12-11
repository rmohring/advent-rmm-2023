fh = open("input11-1.dat")
# fh = open("test.dat")

lines = fh.readlines()
rows = [x.strip("\n") for x in lines]

NUMROWS = len(rows)
NUMCOLS = len(rows[0])
print("orig", NUMROWS, NUMCOLS)

newrows = []
for row in rows:
    newrows.append(list(row))
    if "#" not in row:
        newrows.append(list(row))

NUMROWS = len(newrows)
NUMCOLS = len(newrows[0])
print("exp1", NUMROWS, NUMCOLS)

transp = []
for i in range(NUMCOLS):
    tmp = []
    for j in range(NUMROWS):
        tmp.append(newrows[j][i])
    transp.append(tmp.copy())

newtransp = []
for row in transp:
    newtransp.append(list(row))
    if "#" not in row:
        newtransp.append(list(row))

NUMTROWS = len(newtransp)
NUMTCOLS = len(newtransp[0])
print("transp+exp2", NUMTROWS, NUMTCOLS)

final = []
for i in range(NUMTCOLS):
    tmp = []
    for j in range(NUMTROWS):
        tmp.append(newtransp[j][i])

    final.append(tmp.copy())

NUMROWS = len(final)
NUMCOLS = len(final[0])
print("final", NUMROWS, NUMCOLS)

galaxies = []
for i in range(NUMCOLS):
    for j in range(NUMROWS):
        if final[j][i] != ".":
            galaxies.append((j, i))

print(galaxies)

total = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        dist = abs(x2 - x1) + abs(y2 - y1)
        # print(i, j, galaxies[i], galaxies[j], dist)
        total += dist

print("Answer =", total)

# for row in final:
#     print("".join(row))
