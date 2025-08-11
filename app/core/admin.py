from django.contrib import admin
from app.core.models import *

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SaleDate)
