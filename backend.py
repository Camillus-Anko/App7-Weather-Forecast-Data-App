import requests

API_KEY = "cd912406d6cd0b78c29022e628ee0ca6"

def get_data(place, forecast_days=None, kind=None):

    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)

    data = response.json()

    return data





if __name__ == "__main__":
    print(get_data(place="Tokyo"))