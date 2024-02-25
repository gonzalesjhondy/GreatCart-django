from django.shortcuts import render, get_object_or_404
from .models import Product
from .models import category
# Create your views here.

def store(Request, category_slug=None):
    categories = None
    products = None

    if(category_slug != None):
        categories = get_object_or_404(category, slug = category_slug)
        products = Product.objects.all().filter(category=categories,is_available=True)
        product_count = products.count(); #the use of count is to count data inside the products
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    context = {
        'products': products,
        'countProducts' : product_count,
    } 
    return render(Request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):

    single_product = Product.objects.get(category__slug=category_slug, slug=product_slug) 

    context = {
        'single_product': single_product,
    }
    return render(request, 'store/product_detail.html', context)