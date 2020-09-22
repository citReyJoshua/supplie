from django.db import models
from backend import globals


class Product(models.Model):
    name = models.CharField(verbose_name='Product Name', max_length=globals.MAX_LENGTH_DEFAULT)
    category = models.CharField(max_length=globals.MAX_LENGTH_SHORT)
    brand = models.CharField(max_length=globals.MAX_LENGTH_SHORT, blank=True, null=True)
    color = models.CharField(max_length=globals.MAX_LENGTH_SHORT, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_stocks = models.PositiveIntegerField()

    def __str__(self):

        return self.name


class ProductImage(models.Model):
    image = models.ImageField(upload_to='frontend/static/images/product/product-images', verbose_name='Product Image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
