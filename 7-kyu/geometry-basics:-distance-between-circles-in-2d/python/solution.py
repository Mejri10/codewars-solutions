def distance_between_circles(a, b):
    d = ((b.center.x-a.center.x)**2 + (b.center.y-a.center.y)**2)**.5
    return d - (a.radius+b.radius) if (a.radius+b.radius < d) else 0
