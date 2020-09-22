from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import CustomerRegistrationForm


class CustomerView(View):
    def get(self, request):
        return render(request, 'customer/index.html')


class CustomerRegistrationView(View):

    def get(self, request):
        return render(request, 'registration/customer/index.html')

    def post(self, request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/customer/')

        print('Invalid request.')
        return HttpResponse(form.errors)


class LandingPage(View):
    def get(self, request):
        return render(request, 'landingpage/index.html')
