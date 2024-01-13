from django.urls import path
from . import views

app_name = "blog"


urlpatterns = [
    path("", views.PostListView.as_view(), name="home"),
    path("detail/<slug:slug>/", views.PostDetailView.as_view(), name="detail"),
    path("create/", views.PostUploadView.as_view(), name="create"),
    path("categories/<str:name>/", views.category, name="category"),
    path("tags/<str:name>/", views.tag, name="tag"),

]
