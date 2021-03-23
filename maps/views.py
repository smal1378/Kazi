from django.shortcuts import render
from .models import Map
# Create your views here.


def home_view(request):
    maps = Map.objects.order_by("-rank")
    return render(request, "maps/home.html", {"maps": maps})

