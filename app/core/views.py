from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def home(request):
    data = {
        'Name': 'Norbey'
    }
    return render(request, 'index.html', data)
