from django.urls import path
from . import views

app_name ="mark"

urlpatterns = [
     path('index/', views.index, name="index"),
     path('create/', views.create, name="create"),
     path('delete/<bpk>', views.delete, name="delete")
]