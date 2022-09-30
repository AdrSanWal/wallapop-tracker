from django.shortcuts import render

# from core.models import Filters


def home(request):
    return render(request, 'tracker/home.html')
