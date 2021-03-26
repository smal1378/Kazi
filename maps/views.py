from django.shortcuts import render
from .models import Map
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.urls import reverse

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


def login_view(request):
    if request.user.is_authenticated:
        return render(request, "maps/already_login.html", {"user": request.user.username})
    if request.method == "POST":
        if "username" in request.POST and "password" in request.POST:
            user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, "maps/login.html", {"error": 1})
        else:
            return HttpResponseBadRequest(render(request, "maps/bad_request.html").getvalue())
    else:
        return render(request, "maps/login.html", {"error": 0})


def profile_view(request):
    pass


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

