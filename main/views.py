from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def information(request):
    return render(request, 'information.html')

def program(request):
    return render(request, 'program.html')

