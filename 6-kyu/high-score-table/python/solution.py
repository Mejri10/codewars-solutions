class HighScoreTable:
    
    def __init__(self, size):
        self.size = size
        self.scores = []
    
    def update(self, score):
        if len(self.scores) < self.size:
            self.scores.append(score)
        else:
            lowest = min(self.scores)
            if score > lowest:
                self.scores[self.scores.index(lowest)] = score              
        self.scores.sort(reverse=True)
    
    def reset(self):
        self.scores = []
