from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import logout
from django.views import generic
from django.urls import reverse_lazy


class Register(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("account:login")
    template_name = "account/register.html"


class Logout(generic.View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("account:login")

# def register(request):
#     if request.method == "POST":
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("account:login")
#     else:
#         form = RegisterForm()
#
#     return render(request,
#                   "account/register.html",
#                   {
#                       "form": form,
#                    }
#                   )


# def user_logout(request):
#     logout(request)
#     return redirect("account:login")
