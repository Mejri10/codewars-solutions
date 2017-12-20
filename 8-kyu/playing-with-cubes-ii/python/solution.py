class Cube:
    def __init__(self, side=0):
        self.side = side

    def get_side(self):
        return self.side
	
    def set_side(self, new_side):
        self.side = abs(new_side)
