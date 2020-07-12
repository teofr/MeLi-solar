from math import sqrt

def distance(a, b):
    # The distance between two coordinates
    (x1, y1) = a
    (x2, y2) = b
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)

def feq(a, b, eps=1e-7):
    # Comparison between floats
    return abs(a-b) <= eps
