from django.urls import path

from .views import PlacesView, PlaceView

urlpatterns = [
    path('', PlacesView.as_view(), name="places_repository"),
    path('place/<int:pk>/', PlaceView.as_view(), name="place_view")
]
