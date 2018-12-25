from django.urls import path
from .views import (
    home,
    all,
)

app_name = "products"
urlpatterns = [
    path('', home, name='home'),
    path('products/', all, name='all')
]
