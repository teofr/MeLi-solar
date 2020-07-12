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
        if Planet.collinearWithOrigin(self.planets[0], self.planets[1], self.planets[2]):
            return Drought()
        elif Planet.collinear(self.planets[0], self.planets[1], self.planets[2]):
            return Optimal()
        elif Planet.includeOrigin(self.planets[0], self.planets[1], self.planets[2]):
            dists = [ 
                distance(self.planets[i].coord(), self.planets[(i+1)%3].coord()) 
                    for i in range(3)
            ]
            return Rainy(sum(dists))
        else:
            return Unknown()
