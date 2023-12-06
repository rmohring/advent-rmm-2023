fh = open("input6-1.dat", "r")

lines = fh.readlines()
tot_time = lines[0].strip("\n").split(":")[1].split()
record = lines[1].strip("\n").split(":")[1].split()

answer = 1
for T, R in zip(tot_time, record):
   ways = 0
   for ts in range(int(T)):
      dist = ts*(int(T)-ts)
      if dist>int(R):
         ways += 1
   print(ways)
   answer *= ways

print(answer)