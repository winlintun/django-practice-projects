from django.urls import path
from . import views


app_name = "task"


urlpatterns = [

    path("", views.TaskHomeView.as_view(), name="home"),
    path("create/", views.TaskAddView.as_view(), name="add"),
    path("<int:pk>/complete/", views.CompleteTaskView.as_view(), name="complete"),
    path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="delete")

]
