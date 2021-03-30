from django.urls import path
from .views import home_view, login_view, profile_view, logout_view, signup_view

urlpatterns = [
    path("", home_view, name="home"),
    path("login/", login_view, name="login"),
    path("profile/", profile_view, name="profile"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup_view, name="signup"),
]