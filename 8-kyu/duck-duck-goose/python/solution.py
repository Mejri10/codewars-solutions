from itertools import cycle

def duck_duck_goose(players, goose):
    for i, player in enumerate(cycle(players)):
        if i == goose - 1:
            return player.name