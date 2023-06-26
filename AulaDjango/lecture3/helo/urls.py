from django.urls import path
from . import views

urlpatterns =[
    path("",views.index, name="index"),
    path("<str:name>",views.greet, name="greet"),
    path("paulo",views.paulo, name="paulo"),
    path("renato",views.renato, name="renato"),
]