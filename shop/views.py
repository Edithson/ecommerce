from django.shortcuts import render
from .models import Category, Product
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    search_text = request.GET.get('search-text', '')
    #filtrage selon le nom ou la description du produit
    if search_text and search_text != '' and search_text is not None:
        products = products.filter(name__icontains=search_text)

    # Pagination des produits
    paginator = Paginator(products, 8)  #  8 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': categories,
        'products': page_obj
    }
    return render(request, 'shop/index.html', context)