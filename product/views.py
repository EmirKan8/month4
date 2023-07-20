from django.shortcuts import render
from product.models import Category, Product


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context = {
            'products': products
        }

    return render(request, "products/products.html", context=context)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context = {
            'categories': categories
        }

    return render(request, "products/products.html", context=context)