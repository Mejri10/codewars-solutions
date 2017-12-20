def strong_enough( earthquake, age ):
	magnitude = reduce(lambda x, y: x*y, [sum(i) for i in earthquake])
	strength = 0.99**age * 1000
	return "Safe!" if magnitude < strength else "Needs Reinforcement!"