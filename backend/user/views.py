from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import CustomerRegistrationForm
from .models import Customer
from .choices import CHOICES_STATUS as status_choices, CHOICES_GENDER as gender_choices


class CustomerView(View):

    def get(self, request):
        customers = Customer.objects.all()  # pylint: disable=no-member
        context = {
            'customers': customers,
        }
        return render(request, 'customer/index.html', context)


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
