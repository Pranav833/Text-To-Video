from . import views
from django.urls import path

urlpatterns = [

    path('index', views.index, name='index'),
        path('input', views.get_input, name='input')
]