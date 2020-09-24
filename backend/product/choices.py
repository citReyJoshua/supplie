from django.db import models


class Category(models.TextChoices):
    CLOTHING = ('CL', 'Clothing')
    COSMETICS = ('CO', 'Cosmetics')
    GARDENING = ('GA', 'Gardening')
    HARDWARE = ('HH', 'Hardware')
    HOME_APPLIANCE = ('HA', 'Home Appliance')
    HOUSEWARE = ('HO', 'Houseware')
    SPORTING_GOODS = ('SG', 'Sporting Goods')
    TOILETRIES = ('TO', 'Toiletries')


class Color(models.TextChoices):
    RED = ('R', 'Red')
    ORANGE = ('O', 'Orange')
    YELLOW = ('Y', 'Yellow')
    GREEN = ('G', 'Green')
    BLUE = ('BU', 'Blue')
    VIOLET = ('V', 'Violet')
    WHITE = ('W', 'White')
    BLACK = ('BL', 'Black')
