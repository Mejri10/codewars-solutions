from random import choice

class Ghost(object):
    
    COLORS = ['white', 'yellow', 'purple', 'red']
    
    def __init__(self):
        self.color = choice(self.COLORS)