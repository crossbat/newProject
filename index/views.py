from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'index.html')

def eventNews(request):
    return render(request, "eventNews.html")

def test(request):
    return render(request, "test.html")
