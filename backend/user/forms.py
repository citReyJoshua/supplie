from django import forms
from .models import Customer, Transaction


class CustomerRegistrationForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = ['quantity', 'product', 'customer', 'cash_received']
