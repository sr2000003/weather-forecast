from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = {}  # Always initialize
    if request.method == 'POST':
        city = request.form.get('city')
        api_key = 'addc93500106b9a5036a581a57aa14dc'  # ✅ AAPKI KEY
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            res = requests.get(url)
            res.raise_for_status()
            data = res.json()
            weather_data = {
                'city': city,
                'temp': data['main']['temp'],
                'desc': data['weather'][0]['description']
            }
        except requests.exceptions.HTTPError:
            weather_data['error'] = "City not found. Enter a valid city name."
        except Exception as e:
            weather_data['error'] = f"An error occurred: {e}"

    return render_template('weather.html', data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)

