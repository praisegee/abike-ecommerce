from unicodedata import name
from .helpers.generate_id import generate_id
from django.shortcuts import render
from .models import *


def store(request, *args, **kwargs):
    products = Product.objects.all()
    if request.method == "GET":
        search = request.GET.get("search")
        if search is not None:
            search = search.strip()
            products = Product.objects.filter(name__icontains=search)
    context = {"products": products}
    return render(request, "store/store.html", context)

def product(request, product_id, *args, **kwargs):
    product = Product.objects.get(product_id=product_id)
    context = {"product": product}
    return render(request, "store/product.html", context)
    
def cart(request, *args, **kwargs):
    context = {}
    return render(request, "store/cart.html", context)

def checkout(request, *args, **kwargs):
    context = {}
    return render(request, "store/checkout.html", context)

def user_login(request, *args, **kwargs):
    return render(request, "store/login.html", {})