from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('ev', views.eventNews),
    path('test', views.test)
]
