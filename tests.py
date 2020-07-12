import unittest
from math import atan2, degrees

from src.planet import Planet
from src.solarSystem import SolarSystem
from src.auxmath import feq, distance

class PlanetTests(unittest.TestCase):
    class PlanetDummy(Planet):
        def __init__(self, dist, angle):
            Planet.__init__(self, dist, 0)
            self.angle = angle

    class PlanetDummyCoord(Planet):
        def __init__(self, coord):
            d = distance(coord, (0, 0))
            angle = degrees(atan2(coord[0], coord[1]))
            Planet.__init__(self, d, 0)
            self.angle = angle

    def assertPairAlmostEqual(self, a, b):
        self.assertTrue(feq(a[0], b[0]) and feq(a[1], b[1]))

    def test_moves(self):
        mov = 23
        p = Planet(dist = 100, mov = mov)
        p.advance()
        self.assertEqual(p.angle, mov)
        p.advance(3)
        self.assertEqual(p.angle, mov*4)

    def test_coord(self):
        p = Planet(dist = 100, mov = 1)
        self.assertPairAlmostEqual(p.coord(), (0, 100))
        p.advance(90)
        self.assertPairAlmostEqual(p.coord(), (100, 0))
        p.advance(180)
        self.assertPairAlmostEqual(p.coord(), (-100, 0))
    
    def test_coord_dummy(self):
        p = self.PlanetDummyCoord((25, 34))
        self.assertPairAlmostEqual(p.coord(), (25, 34))

    def test_collinear(self):
        p1 = self.PlanetDummyCoord((10, 0))
        p2 = self.PlanetDummyCoord((10, 3))
        p3 = self.PlanetDummyCoord((10, 10))

        self.assertTrue(Planet.collinear(p1, p2, p3))
    
    def test_collinear_with_origin(self):
        p1 = self.PlanetDummy(100, 20)
        p2 = self.PlanetDummy(10000, 20)
        p3 = self.PlanetDummy(10220, 200)

        self.assertTrue(Planet.collinearWithOrigin(p1, p2, p3))

        p1 = self.PlanetDummyCoord((34, 34))
        p2 = self.PlanetDummyCoord((10000, 10000))
        p3 = self.PlanetDummyCoord((-3, -3))

        self.assertTrue(Planet.collinearWithOrigin(p1, p2, p3))

    def test_include_origin(self):
        p1 = self.PlanetDummyCoord((0, 20))
        p2 = self.PlanetDummyCoord((10000, 0))
        p3 = self.PlanetDummyCoord((-10220, 0))

        self.assertTrue(Planet.includeOrigin(p1, p2, p3))

        p1 = self.PlanetDummyCoord((0, 20))
        p2 = self.PlanetDummyCoord((10000, 1))
        p3 = self.PlanetDummyCoord((-1, 2))

        self.assertFalse(Planet.includeOrigin(p1, p2, p3))

        p1 = self.PlanetDummyCoord((34, 34))
        p2 = self.PlanetDummyCoord((0, -10))
        p3 = self.PlanetDummyCoord((-3, 3))

        self.assertTrue(Planet.includeOrigin(p1, p2, p3))


class SystemTests(unittest.TestCase):
    class PlanetDummyAdvance():
        def __init__(self):
            self.advances = 0
        
        def advance(self, days = 1):
            self.advances += days

    def test_advance(self):
        s = SolarSystem()
        s.planets = [self.PlanetDummyAdvance(), self.PlanetDummyAdvance(), self.PlanetDummyAdvance()]

        s.advance()
        for p in s.planets:
            self.assertEqual(p.advances, 1)
        
        s.advance(4)
        for p in s.planets:
            self.assertEqual(p.advances, 5)
        



if __name__ == '__main__':
    unittest.main()