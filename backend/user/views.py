from django.shortcuts import render, redirect, reverse
from django.views import View
from django.http import HttpResponse
from backend.product.models import Product, ProductImage
from .forms import CustomerRegistrationForm, TransactionForm
from .models import Customer, Transaction
from .choices import CHOICES_STATUS as status_choices, CHOICES_GENDER as gender_choices


class CustomerView(View):

    def get(self, request):
        customers = Customer.objects.all()  # pylint: disable=no-member
        context = {
            'customers': customers,
            'status_choices': status_choices,
            'gender_choices': gender_choices,
        }
        return render(request, 'customer/index.html', context)

    def post(self, request):
        if 'btndelete' in request.POST:
            id = int(request.POST.get("btndelete"))
            Customer.objects.get(id=id).delete()  # pylint: disable=no-member
        elif 'btnupdate' in request.POST:
            id = int(request.POST.get('btnupdate'))
            customer_instance = Customer.objects.get(
                id=id)  # pylint: disable=no-member
            form = CustomerRegistrationForm(request.POST, request.FILES,
                                            instance=customer_instance)
            if form.is_valid():
                form.save()

        return redirect('/customer/#')


class CustomerRegistrationView(View):

    def get(self, request):
        context = {
            'status_choices': status_choices,
            'gender_choices': gender_choices,
        }
        return render(request, 'registration/customer/index.html', context)

    def post(self, request):
        form = CustomerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/customer/')

        return HttpResponse(form.errors)


class LandingPage(View):

    def get(self, request):
        return render(request, 'landingpage/index.html')


class ProductOrderView(View):
    def get(self, request):
        products = Product.objects.all()  # pylint: disable=no-member
        product_images = ProductImage.objects.all()  # pylint: disable=no-member
        customer = Customer.objects.all()  # pylint: disable=no-member
        context = {
            'customers': customer,
            'products': products,
            'product_images': product_images
        }
        return render(request, 'buy/index.html', context)

    def post(self, request):
        form = TransactionForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cash_received = form.cleaned_data['cash_received']
            customer = form.cleaned_data['customer']
            product = form.cleaned_data['product']

            # product = Product.objects.get(id=int(product_id))  # pylint: disable=no-member
            # customer = Customer.objects.get(id=customer_id)  # pylint: disable=no-member

            total_price = product.price * quantity
            cash_change = cash_received - total_price

            if cash_change < 0:
                return HttpResponse('<b> negative change </b>')

            transaction = Transaction(cash_received=cash_received,
                                      cash_change=cash_change,
                                      product=product,
                                      customer=customer,
                                      quantity=quantity)
            transaction.save()
            return redirect('/customer/order/#')

        return form.errors
