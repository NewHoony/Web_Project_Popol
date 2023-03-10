from django.urls import path
from .import views

app_name = "main"


urlpatterns = [

    path("index/",views.index,name="index"),
    path("login/",views.login_user, name ="login"),
    path("logout/",views.logout_user, name ="logout"),
    path("signup/",views.signup, name ="signup"),
    path("profile/",views.profile, name ="profile"),
    path("update/",views.update, name ="update"),
    path("delete/",views.delete, name ="delete")

]