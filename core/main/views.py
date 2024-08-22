from django.shortcuts import render, get_object_or_404
from .models import Logo, Slide, Category, Product, Tag

# Existing index view
def index(request):
    logo = Logo.objects.first() 
    slides = Slide.objects.all()
    categories = Category.objects.all()
    products = Product.objects.all()
    tags = Tag.objects.all()
    return render(request, 'index.html', context={
        'logo': logo,
        'slides': slides,
        'categories': categories,
        'products': products,
        'tags': tags
    })

# New product_list view
def product_list(request, category_id):
    # Retrieve products by category_id
    products = Product.objects.filter(category_id=category_id)
    # Retrieve categories to include in the context
    categories = Category.objects.all()
    return render(request, 'product_list.html', context={
        'products': products,
        'categories': categories
    })

# New product_detail view
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})
