from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.pk} | {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField()
    amount = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return f'{self.pk} | {self.name}'
