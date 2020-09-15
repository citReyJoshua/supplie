from django.db import models
from backend import globals
from . import choices


class Person(models.Model):

    first_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT)
    middle_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, blank=True, default='')
    last_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT)
    profile_pic = models.ImageField(upload_to='frontend/static/images/customer/profile-pics/')
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=globals.MAX_LENGTH_LONG)
    status = models.CharField(max_length=globals.MAX_LENGTH_SHORT,
                              choices=choices.CHOICES_STATUS, default=choices.SINGLE)
    gender = models.CharField(max_length=globals.MAX_LENGTH_SHORT,
                              choices=choices.CHOICES_GENDER, default=choices.NOT_SPECIFIED)
    no_of_children = models.PositiveIntegerField(default=0)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()

    # address fields
    city = models.CharField(max_length=globals.MAX_LENGTH_SHORT)
    province = models.CharField(max_length=globals.MAX_LENGTH_SHORT)
    brgy = models.CharField(verbose_name='Barangay', max_length=globals.MAX_LENGTH_SHORT)
    country = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT)
    zip_code = models.PositiveIntegerField()

    # spouse fields
    spouse_first_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    spouse_last_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    spouse_occupation = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)

    # parent's fields
    father_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    father_occupation = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    mother_name = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)
    mother_occupation = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)

    height = models.FloatField(verbose_name='Height (cm)')
    weight = models.FloatField(verbose_name='weight (kg)')
    religion = models.CharField(max_length=globals.MAX_LENGTH_DEFAULT, null=True, blank=True)

    class Meta:
        db_table = 'Person'

    def __str__(self):
        return self.last_name + ', ' + self.first_name + self.middle_name


class Customer(Person):

    date_registered = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Customer'

    def __str__(self):
        return super.__str__()
