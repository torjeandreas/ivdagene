from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')


def information(request: HttpRequest) -> HttpResponse:
    return render(request, 'information.html')


def program(request: HttpRequest) -> HttpResponse:
    return render(request, 'program.html')


def registration(request: HttpRequest) -> HttpResponse:
    return render(request, 'registration.html')
