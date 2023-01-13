from django.urls import path
from .import views

app_name = "note"

urlpatterns = [

    path("index/",views.index, name="index"),
    path("show/<bpk>",views.show, name = 'show'),
    path("delete/<bpk>",views.delete, name = 'delete'),
    path("create/",views.create, name = 'create'),
    path("update/<bpk>",views.update, name = 'update'),
    path("likey/<bpk>",views.likey, name ="likey"),
    path("unlikey/<bpk>",views.unlikey, name ="unlikey"),
    path('creply/<bpk>', views.creply, name ='creply'),
    path('dreply/<bpk><rpk>',views.dreply, name ='dreply'),

]