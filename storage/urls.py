from django.urls import path
from . import views

app_name ="storage"


urlpatterns = [

    path("index/", views.index, name="index"),
    path("upload/", views.upload, name="upload"),
    path("show/<ipk>", views.show, name="show"),
    path("delete/<ipk>", views.delete, name="delete"),





]