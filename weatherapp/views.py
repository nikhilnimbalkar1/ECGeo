import requests

from django.views.generic import ListView, CreateView, TemplateView, UpdateView

from .forms import CreatePlaceForm
from .models import Place


class PlacesView(ListView):
    model = Place
    template_name = "geo_places.html"
    context_object_name = 'objs'


class PlaceView(UpdateView):
    model = Place
    context_object_name = 'obj'
    slug_field = 'pk'
    template_name = 'geo_place.html'
    form_class = CreatePlaceForm

    def get_forecast(self):
        res = requests.get(f"https://api.weather.gov/points/{self.object.location.y},{self.object.location.x}")
        if res.status_code == 200:
            forecast_url = res.json().get('properties', {}).get('forecast')
            if forecast_url:
                r = requests.get(forecast_url)
                if r.status_code == 200:
                    return r.json().get('properties', {}).get('periods', {})
        return "Could not get weather forecast"

    def get_context_data(self, **kwargs):
        ctx = super(PlaceView, self).get_context_data()
        ctx['forecast'] = self.get_forecast()
        return ctx



