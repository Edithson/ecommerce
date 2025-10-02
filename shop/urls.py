
from django.urls import path
from shop.views import index, show, panier

urlpatterns = [
    path('', index, name='index'),
    path('produit/<int:product_id>/', show, name='show'),
    path('panier/', panier, name='panier'),
]