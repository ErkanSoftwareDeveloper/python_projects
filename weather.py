import requests

API_KEY = "API_KEY"


def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching weather data.")
        return

    data = response.json()

    print("\n Weather Report")
    print("----------------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Conditions:", data["weather"][0]["description"])


city = input("Enter city name: ")
get_weather(city)
