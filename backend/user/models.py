from django.db import models
from backend.product.models import Product
from backend import globals
from . import choices


class Person(models.Model):

    # main fields
    first_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT)
    middle_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    last_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    profile_pic = models.ImageField(upload_to='frontend/static/images/customer/profile-pics/',
                                    blank=True, default='frontend/static/images/assets/add-image.jpg')
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=globals.MAX_LENGTH_LONG, null=True, blank=True)
    status = models.CharField(max_length=globals.MAX_LENGTH_SHORT,
                              choices=choices.CHOICES_STATUS, default=choices.SINGLE)
    gender = models.CharField(max_length=globals.MAX_LENGTH_SHORT,
                              choices=choices.CHOICES_GENDER, default=choices.NOT_SPECIFIED)
    no_of_children = models.PositiveIntegerField(default=0)

    # address fields
    brgy = models.CharField(verbose_name='Barangay', max_length=globals.MAX_LENGTH_SHORT)
    province = models.CharField(max_length=globals.MAX_LENGTH_SHORT)
    city = models.CharField(max_length=globals.MAX_LENGTH_SHORT)
    country = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT)
    zip_code = models.PositiveIntegerField()

    # spouse fields
    spouse_first_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    spouse_last_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    spouse_occupation = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)

    # parent's fields
    father_first_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    father_last_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    father_occupation = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    mother_first_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    mother_last_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    mother_occupation = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)

    height = models.FloatField(verbose_name='Height (cm)', blank=True, null=True)
    weight = models.FloatField(verbose_name='weight (kg)', blank=True, null=True)
    religion = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)

    class Meta:
        db_table = 'Person'

    def __str__(self):

        return self.last_name + ', ' + self.first_name


class Customer(Person):

    date_registered = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Customer'


class Transaction(models.Model):

    # date field
    date = models.DateField(auto_now_add=True)

    # cash fields
    cash_received = models.DecimalField(max_digits=10, decimal_places=2)
    cash_change = models.DecimalField(max_digits=10, decimal_places=2)

    # foreign fields
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)

    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = 'Transaction'

    def __str__(self):
        return f'{self.quantity} piece/s of {self.product.name} bought by {self.customer.first_name} {self.customer.last_name}'  # pylint: disable=no-member
