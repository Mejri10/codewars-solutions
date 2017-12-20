def cross_product(a, b):
    vx = a.y*b.z - a.z*b.y
    vy = a.z*b.x - a.x*b.z
    vz = a.x*b.y - a.y*b.x
    return Vector(vx, vy, vz)
