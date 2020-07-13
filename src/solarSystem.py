from src.planet import Planet
from src.auxmath import *
from src.weather import *

class SolarSystem:
    # The SolarSystem class models a solar system of 3 given planets

    def __init__(self):
        self.planets = [Planet(1000, -5), # Vulcano
                        Planet(2000, 3),  # Betasoide
                        Planet(500, 1)]   # Ferengi
    
    def advance(self, days = 1):
        for p in self.planets:
            p.advance(days)
    
    def weather(self):
        if self.collinearWithSun():
            return Drought()
        elif Planet.collinear(self.planets[0], self.planets[1], self.planets[2]):
            return Optimal()
        elif self.includeSun():
            dists = [ 
                distance(self.planets[i].coord(), self.planets[(i+1)%3].coord()) 
                    for i in range(3)
            ]
            return Rainy(sum(dists))
        else:
            return Unknown()

    def collinearWithSun(self):
        # Checks whether the planets are collinear with the Sun
        # It's better than Planet.collinear(...) since it doesn't
        # compare floats, only ints

        ps = self.planets

        if len(ps) <= 1:
            # Trivial case
            return True
        
        return all((ps[0].angle % 180) == (p.angle % 180) for p in ps[1:])
    
    def includeSun(self):
        # Checks whether the Sun is included on the triangle
        # formed by the three planets

        if len(self.planets) != 3:
            raise 'Inclusion of the Sun is only implemented for 3 planets'

        (p1, p2, p3) = sorted([p.angle for p in self.planets])

        if p2 - p1 > 180:
            # Notice that p3 - p1 is also > 180
            return False
        
        if p3 - p1 >= 180 and p3 - p2 <= 180:
            return True
        else:
            return False