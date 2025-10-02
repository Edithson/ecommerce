from django.shortcuts import render
from .models import Category, Product, Commande
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

def show(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product': product
    }
    return render(request, 'shop/show.html', context)

def panier(request):
    if request.method == "POST":
        items = request.POST.get("articles")
        nom_prenom = request.POST.get("nom_prenom")
        email = request.POST.get("email")
        adresse = request.POST.get("adresse")
        telephone = request.POST.get("telephone")
        # Traitement des données du formulaire
        commande = Commande(
            items=items,
            nom_prenom=nom_prenom,
            email=email,
            adresse=adresse,
            telephone=telephone
        )
        commande.save()
        # Vous pouvez ajouter un message de succès ou rediriger vers une autre page

    return render(request, 'shop/panier.html')