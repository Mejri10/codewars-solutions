from math import acos, pi

def triangle_type (a, b, c):
  a, b, c = sorted([float(a), float(b), float(c)], reverse=True)
  # Triangle Inequality
  if a >= b + c:   
    return 0
  # Pythagorean Thereom
  elif a**2 == b**2 + c**2: 
    return 2
  # Checks if greater angle is less than 90 degrees
  elif acos((b**2 + c**2 - a**2)/(2*b*c)) < pi/2: 
    return 1
  else:
    return 3