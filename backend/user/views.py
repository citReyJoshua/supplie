from django.shortcuts import render
from django.views import View

class CustomerView(View):
    def get(self, request):
        return render(request, 'customer/index.html')


class CustomerRegistrationView(View):
    def get(self, request):
        return render(request,'registration/customer/index.html')

class LandingPage(View):
    def get(self, request):
        return render(request,'landingpage/index.html')
