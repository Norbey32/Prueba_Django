
from django.urls import path
from app.core.views import home

urlpatterns = [
    path('uno', home),
    path('dos', home)
]
