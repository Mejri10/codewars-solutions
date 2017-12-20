def triangle_area(t):
    return abs(t.a.x*(t.b.y-t.c.y) + t.a.y*(t.c.x-t.b.x) + t.b.x*t.c.y-t.b.y*t.c.x)/2