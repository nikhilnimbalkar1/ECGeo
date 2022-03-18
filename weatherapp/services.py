import requests


class WeatherApi:
    def __init__(self, location):
        self.lat = location.y
        self.long = location.x
        self.api_url = f"https://api.weather.gov/points/{self.lat},{self.long}"

    def get_api_url(self):
        return self.api_url

    def get_forecast_url(self):
        url = None
        res = requests.get(self.get_api_url())
        if res.status_code == 200:
            url = res.json().get('properties', {}).get('forecast')
        return url

    def get_forecast(self):
        forecast_url = self.get_forecast_url()
        forecast = None
        if forecast_url:
            r = requests.get(forecast_url)
            if r.status_code == 200:
                forecast = r.json().get('properties', {}).get('periods', {})
        return forecast

