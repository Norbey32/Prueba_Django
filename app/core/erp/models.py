from django.db import models
import os

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dni = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        crm_table = "Cliente"
        ordering = ["id"]

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        crm_table = "Categoria"
        ordering = ["id"]

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        crm_table = "Producto"
        ordering = ["id"]

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_sale = models.DateTimeField(default=models.DateTimeField.now)
    subtotal = models.DecimalField(max_length=10, decimal_palaces=2)
    iva = models.DecimalFiel(max_length=10, decimal_places=2)
    total = models.DecimalField(max_length=10, decimal_places=2)

    def __str__(self):
        return f"Venta {self.id} - {self.customer}"
    
    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"
        crm_table = "Venta"
        ordering = ["id"]

class SaleDate(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle de Venta {self.id} - {self.sale} - {self.product}"
    
    class Meta:
        verbose_name = "Detalle de Venta"
        verbose_name_plural = "Detalles de Venta"
        crm_table = "DetalleVenta"
        ordering = ["id"]
