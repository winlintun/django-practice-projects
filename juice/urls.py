from django.urls import path
from . import views

app_name = "juice"


urlpatterns = [
    path("", views.juice_list, name="list"),
    path("cart/", views.view_card, name="cart"),
    path("add_to_cart/<slug:juice_slug>/", views.add_to_cart, name="add_cart"),
    path("remove_form_cart/<slug:juice_slug>/", views.remove_to_cart, name="remove_cart"),
    path("checkout/", views.checkout, name="checkout"),

]
