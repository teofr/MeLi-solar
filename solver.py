from src.solarSystem import SolarSystem
from src.auxmath import feq


def calculate(years = 10):
    # Calculate the number of weather predictions for the given years

    # TODO: check years validity
    s = SolarSystem()

    ws = {"Lluvia" : 0,
          "Sequia" : 0,
          "Optimo" : 0,
          "Desconocido" : 0}

    maxRainyDays = []
    maxRain = -1

    daysPerYear = 365

    for day in range(years * daysPerYear):
        w = s.weather()
        s.advance()

        ws[w.name()] += 1

        if w.name() == "Lluvia":
            if w.intensity() > maxRain:
                maxRain = w.intensity()
                maxRainyDays = [day]
            elif feq(w.intensity(), maxRain):
                maxRainyDays.append(day)

    return (ws, maxRain, maxRainyDays)

if __name__ == '__main__':

    (ws, maxRain, maxRainyDays) = calculate()
    
    print("Resultados:")
    for w, n in ws.items():
        print("{}: {}".format(w, n))
    
    print("Los dias con más lluvia ({}) fueron {}".format(maxRain, maxRainyDays))
    