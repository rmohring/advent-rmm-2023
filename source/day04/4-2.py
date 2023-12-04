from collections import Counter

fh = open("input4-1.dat", "r")
#fh = open("test.dat", "r")

sum = 0
win_value = {}
num_tix = Counter()
games = fh.readlines()
for game in games:   
    (numstr, groups) = game.strip("\n").split(":")
    game_num = int(numstr.split()[-1])
    (winners, ticket) = groups.split("|")
    winners = set(winners.split())
    ticket = set(ticket.split())
    matches = ticket.intersection(winners)

    num_tix[game_num] = 1
    win_value[game_num] = len(matches)

for game_num in range(1, len(games)+1):
    print(game_num, num_tix[game_num])
    for j in range(num_tix[game_num]):
        for idx in range(game_num+1, game_num+win_value[game_num]+1):
            #print(f"Updating: based on {game_num}, incrementing {idx}, iter {j}")
            num_tix[idx] += 1

# for game_num in range(1, len(games)+1):
#     print("*", game_num, num_tix[game_num], win_value[game_num])
#     sum += num_tix[game_num] * win_value[game_num]

for x,y in num_tix.items():
    sum += y
print(sorted(num_tix.items()))
print(f"Final num cards is: {sum}")
      