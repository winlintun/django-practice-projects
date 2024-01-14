from django.urls import path
from . import views

app_name = "portfolio"


urlpatterns = [
    path("<str:username>/", views.home, name="home"),

]
