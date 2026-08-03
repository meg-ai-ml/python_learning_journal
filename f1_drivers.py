players = [ "max", "lewis", "charles", "kimi", "carlos" ]
print(players)
print(players[0:3])
print(players[1:4])
print(players[:4])
print(players[1:])

print("Here are my top 3 F1 drivers: ")
for player in players[0 : 3]:
    print(player)

scores = list(range(60,105,5))
print(scores)

sorted_scores = sorted( scores , reverse = True )
print(sorted_scores[0:3])
