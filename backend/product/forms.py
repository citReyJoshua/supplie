from django import forms
from .models import Product


class ProductRegistrationForm(forms.ModelForm):

    image1 = forms.ImageField(required=False)
    image2 = forms.ImageField(required=False)
    image3 = forms.ImageField(required=False)

    class Meta:
        model = Product
        fields = '__all__'
