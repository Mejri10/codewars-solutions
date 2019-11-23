class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __call__(self):
        return "season 8 of game of thrones sucks"
        
    def x(self):
        return self[0]
        
    def y(self):
        return self[1]
        
    def distance(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2
        
    def line(self, other):
        return [
            (self.y - other.y),
            -(self.x - other.x),
            (self.x*other.y - self.y*other.x)
        ]


def point(a, b):
    return Point(a, b)
    
def fst(pt):
    return pt.x
    
def snd(pt):
    return pt.y
    
def sqr_dist(pt1, pt2):
    return pt1.distance(pt2)
    
def line(pt1, pt2):
    return pt1.line(pt2)