from django.contrib import admin
from .models import Category, Product

# Register your models here.

# class pour personnaliser l'affichage dans l'admin
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
