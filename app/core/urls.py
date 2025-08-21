
from django.urls import path
from app.core.views.category.views import Category_list
from app.core import views


urlpatterns = [
    path('uno/', Category_list),
]
