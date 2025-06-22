from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def weather():
    weather_data = {}
    if request.method == 'POST':
        city = request.form['city']
        api_key = 'YOUR_OPENWEATHERMAP_API_KEY'
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        res = requests.get(url)
        if res.status_code == 200:
            data = res.json()
            weather_data = {
                'city': city,
                'temp': data['main']['temp'],
                'desc': data['weather'][0]['description']
            }
        else:
            weather_data['error'] = "City not found."
    return render_template('weather.html', data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
