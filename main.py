# [START gae_python38_app]
from flask import Flask, jsonify, request
from src.solarSystem import SolarSystem

app = Flask(__name__)


@app.route('/clima')
def weather():
    day = int(request.args.get('dia'))

    maxYears = 10
    daysPerYears = 365

    if day < 0 or day > maxYears * daysPerYears:
        return 'Wrong request. dia ({}) must be at least 0 and at most {}'.format(
            day,
            maxYears * daysPerYears
        )

    s = SolarSystem()
    s.advance(day)
    w = s.weather()

    response = {
        'dia' : day,
        'clima' : w.name()
    }

    if w.name() == "Lluvia":
        response['intensidad'] = w.intensity()
 
    return jsonify(response)


if __name__ == '__main__':
    # This is used when running locally only.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python38_app]
