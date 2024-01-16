from django.shortcuts import render, get_object_or_404, redirect
from .models import Juice, Order
from .forms import CartForm


def juice_list(request):
    juices = Juice.objects.all()

    return render(request, "juice/list.html", {
        "juices": juices,
    })


def view_card(request):
    order = Order.objects.last()
    return render(request, "juice/view_card.html", {
        "order": order,
    })


def add_to_cart(request, juice_slug):
    juice = get_object_or_404(Juice, slug=juice_slug)
    order, create = Order.objects.get_or_create(total_price=0)

    order.juices.add(juice)
    order.total_price += juice.price
    order.save()
    return redirect("juice:cart")  # view cart


def remove_to_cart(request, juice_slug):
    juice = get_object_or_404(Juice, slug=juice_slug)
    order = Order.objects.last()

    for juice in order.juices.all():
        order.juices.remove(juice)
        order.total_price -= juice.price
        order.save()

    return redirect("juice:cart")


def checkout(request):
    order = Order.objects.last()
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            order.delete()
            return render(request, "juice/checkout_success.html")
    else:
        form = CartForm()

    return render(request, "juice/checkout.html", {
        "form": form,
    })