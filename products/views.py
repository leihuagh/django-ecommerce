from django.shortcuts import render
from .models import Product


def home(request):
    template = "home.html"
    user = request.user
    if request.user.is_authenticated:
        user = request.user.first_name
    context = {
        "user": user,
        "title": 'Welcome to Ecommerce',
        "styles": [
            "/static/css/ecommerce.css"
        ],
        "jss": [
            "/static/js/ecommerce.js"
        ]
    }
    return render(request, template, context)


def all(request):
    products = Product.objects.all()
    template = 'all.html'
    context = {
        "products": products
    }
    return render(request, template, context)
