from django.shortcuts import render


def home(request):
    template = "base.html"
    user = request.user
    if request.user.is_authenticated:
        user = request.user.first_name
    context = {
        "user": user
    }
    return render(request, template, context)
