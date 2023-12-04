fh = open("input4-1.dat", "r")

sum = 0
for game in fh.readlines():   
    (numstr, groups) = game.strip("\n").split(":")
    game_num = int(numstr.split()[-1])
    (winners, ticket) = groups.split("|")
    winners = set(winners.split())
    ticket = set(ticket.split())
    matches = ticket.intersection(winners)
    if matches:
        sum += 2**(len(matches)-1)
    
print(f"Final sum is: {sum}")
      