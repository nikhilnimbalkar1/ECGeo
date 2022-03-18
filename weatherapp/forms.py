from django.contrib.gis import forms
from django.forms import ModelForm

from .models import Place


class CreatePlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))