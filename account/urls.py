from django.urls import path
from . import views
from django.contrib.auth import views as auth_view


app_name = "account"


urlpatterns = [
    path("login/", auth_view.LoginView.as_view(template_name="account/login.html"), name="login"),
    path("register/", views.Register.as_view(), name="register"),
    path("logout/", views.Logout.as_view(), name="logout"),
]
