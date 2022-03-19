from django.contrib import admin

from django.contrib.gis.admin import OSMGeoAdmin
from django.shortcuts import redirect

from .models import Place


@admin.register(Place)
class PlaceAdmin(OSMGeoAdmin, admin.ModelAdmin):
    list_display = ('name', 'location')

    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        # change admin form view
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save_and_add_another'] = False
        extra_context['show_save'] = True
        return super(PlaceAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('places_repository')  # redirect to repo on adding n place
