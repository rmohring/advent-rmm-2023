fh = open("input11-1.dat")
# fh = open("test.dat")

lines = fh.readlines()
rows = [x.strip("\n") for x in lines]

NUMROWS = len(rows)
NUMCOLS = len(rows[0])
print("orig", NUMROWS, NUMCOLS)

newrows = []
for row in rows:
    if "#" in row:
        newrows.append(list(row))
    else:
        newrows.append(["X"] * (len(row)))

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
    if "#" in row:
        newtransp.append(list(row))
    else:
        newtransp.append(["X"] * (len(row)))

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
        if final[j][i] == "#":
            galaxies.append((j, i))

print(galaxies)
# galaxies = galaxies[:2]
total = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        dist = abs(x2 - x1) + abs(y2 - y1)
        dist0 = dist
        # Have to step +1 or -1 depending on which is bigger, x1 or x2
        for chk in range(x1, x2, (x2 > x1) * 2 - 1):
            if final[chk][y2] == "X":
                dist += 999999
        for chk in range(y1, y2, (y2 > y1) * 2 - 1):
            if final[x2][chk] == "X":
                dist += 999999
        # print(i, j, galaxies[i], galaxies[j], dist0, dist)

        total += dist

print("Answer =", total)

# for row in final:
#    print("".join(row))

# ..X#.X..X.
# ..X..X.#X.
# #.X..X..X.
# XXXXXXXXXX
# ..X..X#.X.
# .#X..X..X.
# ..X..X..X#
# XXXXXXXXXX
# ..X..X.#X.
# #.X.#X..X.
