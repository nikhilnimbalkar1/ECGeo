import requests
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import ListView, CreateView, TemplateView, UpdateView

from .forms import CreatePlaceForm
from .models import Place
from .services import WeatherApi


class PlacesView(LoginRequiredMixin, ListView):
    model = Place
    template_name = "geo_places.html"
    context_object_name = 'objs'


class PlaceView(LoginRequiredMixin, UpdateView):
    model = Place
    context_object_name = 'obj'
    slug_field = 'pk'
    template_name = 'geo_place.html'
    form_class = CreatePlaceForm

    def get_context_data(self, **kwargs):
        ctx = super(PlaceView, self).get_context_data()
        forecast_obj = WeatherApi(self.object.location)
        ctx['forecast'] = forecast_obj.get_forecast()
        ctx['forecast_url'] = forecast_obj.get_api_url()
        return ctx



