
class CubeTracker:
    def __init__(self):
        self.m = {'red' : 0, 'green' : 0, 'blue' : 0}
        
    def update(self, color_pull):
        print(color_pull)
        (ncolor, color) = color_pull.strip().split(" ")
        self.m[color] = max(self.m[color], int(ncolor))
    
    def validate(self, nred, ngreen, nblue):
        return ( (self.m['red'] <= nred)
                  and (self.m['green'] <= ngreen)
                  and (self.m['blue'] <= nblue) )
    
    @property
    def power(self):
        return self.m['red']*self.m['green']*self.m['blue']

    def __str__(self):
        return f"RGB max: {self.m}"

fh = open("input2-1.dat", "r")
(NUM_RED, NUM_GREEN, NUM_BLUE) = (12, 13, 14)

sum = 0
for game in fh.readlines():
    ct = CubeTracker()
    success = True
    (numstr, groups) = game.split(":")
    game_num = int(numstr.split(" ")[1])
    for group in groups.split(";"):
        color_pulls = group.split(",")
        for color_pull in color_pulls:
            ct.update(color_pull)
            
    print(game_num, ct)
    sum += ct.power
    
print(f"Final sum is: {sum}")
      