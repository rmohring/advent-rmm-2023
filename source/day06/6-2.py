fh = open("input6-1.dat", "r")

lines = fh.readlines()
tot_time = lines[0].strip("\n").split(":")[1].replace(" ","")
record = lines[1].strip("\n").split(":")[1].replace(" ","")
print(tot_time, record)

ways = 0
for ts in range(int(tot_time)):
   if ts%100000==0:
      print(ts)
   dist = ts*(int(tot_time)-ts)
   if dist>int(record):
      ways += 1
print('-----------')
print(ways)