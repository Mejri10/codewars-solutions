def euclidean_distance(point1, point2):
    partialsum = sum((a - b)**2 for a, b in zip(point1, point2))
    return round(partialsum**.5, 2)