import requests

API_KEY = "dc0ec2ac07fe4d6b84d125953260802"
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def get_weather(city):
    params = {
        "key": API_KEY,
        "q": city,
        "aqi": "no"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error:", response.text)
        return

    data = response.json()

    temperature = data["current"]["temp_c"]
    humidity = data["current"]["humidity"]
    condition = data["current"]["condition"]["text"]

    print("\nWeather Information")
    print("-------------------")
    print(f"City: {data['location']['name']}")
    print(f"Temperature: {temperature} °C")
    print(f"Humidity: {humidity} %")
    print(f"Condition: {condition}")

def main():
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
