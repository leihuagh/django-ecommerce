from django.shortcuts import render


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
