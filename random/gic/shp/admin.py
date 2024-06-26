from django.contrib import admin
from .models import NepalDistrict
from leaflet.admin import LeafletGeoAdmin
# Register your models here.
class NepalDistrictInterface(LeafletGeoAdmin):
    list_display = ["district", "first_stat", "shape_area"]
    def district(self, obj):
        return obj.first_dist
    list_filter = ["shape_area"]
    list_editable = ["shape_area"]
admin.site.register(NepalDistrict, NepalDistrictInterface)