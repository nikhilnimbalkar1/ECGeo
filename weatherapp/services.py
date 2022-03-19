import requests


class WeatherApi:
    def __init__(self, location):
        self.lat = location.y
        self.long = location.x
        self.api_url = f"https://api.weather.gov/points/{self.lat},{self.long}"

    def get_api_url(self):
        return self.api_url

    def get_response(self):
        """
            Get response data from the weather api through location lat and long
        :return: response dict
        """
        data = {
            'url': None
        }
        res = requests.get(self.get_api_url())
        data['api_status'] = res.status_code
        response_data = res.json()
        if res.status_code == 200:
            data['url'] = response_data.get('properties', {}).get('forecast')
        else:
            data.update({
                'error': response_data.get('title'),
                'error_detail': response_data.get('detail')
                }
            )

        return data

    def get_forecast(self):
        """
            Get actual forecasts from the response data
        :return: dict
        """
        data = self.get_response()
        if data.get('api_status') == 200:
            r = requests.get(data.get('url'))
            if r.status_code == 200:
                data.update(
                    {
                        'forecasts': r.json().get('properties', {}).get('periods', {}),
                        'forecast_status': r.status_code
                    }
                )
        return data

