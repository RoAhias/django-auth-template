# users/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import signup_view

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", signup_view, name="signup"),
]
