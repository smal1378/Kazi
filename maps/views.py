from django.shortcuts import render
from .models import Map
# Create your views here.


def home_view(request):
    if request.method == "POST":
        if "prev" in request.POST and request.POST["page"]!="1":
            begin = 5*(int(request.POST["page"])-2)
        elif "next" in request.POST and int(request.POST["page"])*5 < len(Map.objects.all()):
            begin = 5*(int(request.POST["page"]))
        else:
            begin = 5*(int(request.POST["page"])-1)
        maps = Map.objects.order_by("-rank")[begin: begin+5]
        page = request.POST["page"]
    else:
        maps = Map.objects.order_by("-rank")[:5]
        page = 1
    pages = int(len(Map.objects.all()) / 5) + 1
    if request.user.is_authenticated:
        user = request.user.username
    else:
        user = None
    return render(request, "maps/home.html", {"maps": maps, "page": page, "total_pages": pages,
                                              "user": user})



