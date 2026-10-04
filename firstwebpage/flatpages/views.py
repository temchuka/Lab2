from django.shortcuts import render


def home(request):
    return render(request, 'templates/index.html')


def static_handler(request):
    return render(request, 'templates/static_handler.html')
