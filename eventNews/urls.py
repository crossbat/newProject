from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "eventNews"

urlpatterns = [
		path("", views.eventNews, name = "event"),
]
