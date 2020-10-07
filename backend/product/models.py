from django.db import models
from backend import globals
from . import choices


class Product(models.Model):
    date_registered = models.DateField(auto_now_add=True)
    name = models.CharField(verbose_name='Product Name', max_length=globals.MAX_LENGTH_DEFAULT)
    category = models.CharField(max_length=globals.MAX_LENGTH_SHORT, choices=choices.Category.choices)
    brand = models.CharField(max_length=globals.MAX_LENGTH_SHORT, blank=True, null=True)
    color = models.CharField(max_length=globals.MAX_LENGTH_SHORT, blank=True, null=True, choices=choices.Color.choices)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    no_of_stocks = models.PositiveIntegerField()

    class Meta:
        db_table = 'Products'

    def __str__(self):
        return f'#{self.id} - {self.name}'  # pylint: disable=no-member


class ProductImage(models.Model):
    image = models.ImageField(upload_to='frontend/static/images/product/product-images', verbose_name='Product Image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')

    class Meta:
        db_table = 'Product_Image'

    def __str__(self):
        return f'{self.product_id} - image'  # pylint: disable=no-member
