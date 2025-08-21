from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from app.core.models import Category


# Create your views here.


def Category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all(),
    }
    return render(request, 'category/list.html', data)


