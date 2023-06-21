from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.


def sova_index(request: HttpRequest):
    return HttpResponse("привет")
