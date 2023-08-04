from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def eventNews(request):
    return render(request, "eventNews.html")

# Create your views here.
