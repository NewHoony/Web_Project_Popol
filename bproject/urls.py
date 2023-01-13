from django.urls import path
from . import views

app_name = "bproject"

urlpatterns = [

    path("index/", views.index, name="index"),
    path("show/<ipk>", views.show, name="show"),
    path("create/", views.create, name="create"),
    path("delete/<ipk>", views.delete, name="delete"),
    path("update/<ipk>", views.update, name="update"),





]