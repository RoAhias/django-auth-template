# users/urls.py
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import signup_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(
        "login/",
        LoginView.as_view(
            template_name="users/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "logout/", LogoutView.as_view(), name="logout"
    ),
    path(
        "signup/", signup_view, name="signup"
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
