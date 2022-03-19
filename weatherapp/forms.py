from django.contrib.gis import forms
from django.forms import ModelForm

from .models import Place


class CreatePlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = '__all__'

    #  for some reason this doesn't seem to work for multiple django versions
    #  HOTFIX: using admin creation view for new places
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
