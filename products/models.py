from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=None, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=29.99)
    slug = models.SlugField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
