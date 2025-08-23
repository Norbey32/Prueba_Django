
from django.urls import path
from app.core.views.category.views import *

app_name = 'core'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='CategoryListView')
]
