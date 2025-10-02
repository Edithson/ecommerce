from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.
admin.site.site_header = "E-commerce Administration by Edithson"
admin.site.site_title = "GZ Admin"
admin.site.index_title = "Bienvenue dans l'administration E-commerce"

# class pour personnaliser l'affichage dans l'admin
class AdminCategory(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)

class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_at')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)
    list_per_page = 10
    list_editable = ('price', 'category')
    ordering = ['-created_at']

class AdminCommande(admin.ModelAdmin):
    list_display = ('nom_prenom', 'email', 'adresse', 'telephone', 'created_at')
    search_fields = ('nom_prenom', 'email')
    list_per_page = 10
    ordering = ['-created_at']
    #filtrer par email du client
    list_filter = ('email',)

admin.site.register(Category, AdminCategory)
admin.site.register(Product, AdminProduct)
admin.site.register(Commande, AdminCommande)
