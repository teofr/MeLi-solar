# Some possible weather definitions

class Drought:
    def name(self):
        return "Sequia"

class Rainy:
    def __init__(self, intensity):
        self.intensity_ = intensity

    def intensity(self):
        return self.intensity_

    def name(self):
        return "Lluvia"

class Optimal:
    def name(self):
        return "Optimo"

class Unknown:
    def name(self):
        return "Desconocido"
