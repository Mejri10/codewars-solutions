def calculate_score(game):
    x, y = [int(score) for score in game.split(":")]
    return 3 if x > y else 0 if x < y else 1

def points(games):
	return sum(map(calculate_score, games))