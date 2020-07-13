from math import sin, cos, radians
from src.auxmath import *

class Planet:
    # The Planet class models a planet, and provides some
    # static methods meant to be used with Planets only

    def __init__(self, dist, mov):
        self.dist = dist
        self.mov = int(mov)
        self.angle = 0
    
    def advance(self, days = 1):
        # Since the problem only deals with integers, we stay within integers
        if days < 0:
            raise Exception('Cannot advance planets to the past')
        
        self.angle += self.mov*int(days)
        self.angle %= 360
    
    def coord(self):
        # Get the position in coordinate values
        rad = radians(self.angle)
        return (self.dist*sin(rad), self.dist*cos(rad))
    
    @staticmethod
    def collinear(p1, p2, p3):
        # Checks whether 3 planets are collinear by checking
        # if they form a degenerate triangle
        # This method is here since it doesn't involve the Sun
        ps = [p1, p2, p3]
        dists = [distance(ps[i].coord(), ps[(i+1)%3].coord()) for i in range(len(ps))]
        dists.sort()

        return feq(dists[0] + dists[1],  dists[2])
    
    