from django.shortcuts import render
from django.core.serializers import serialize
from .models import NepalDistrict
from django.http import HttpResponse

# Create your views here.
def main(request):
    return render(request, "index.html")

def nepaldata(request):
    nepalData = serialize("geojson", NepalDistrict.objects.all())
    return HttpResponse(nepalData, content_type = "geojson")