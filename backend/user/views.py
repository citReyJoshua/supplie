from django.shortcuts import render
from django.views import View

class CustomerView(View):
    def get(self, request):
        return render(request, 'customer/index.html', {'range': range(50),})