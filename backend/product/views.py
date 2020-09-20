from django.shortcuts import render, redirect
from django.views import View
from . import models
from .forms import ProductRegistrationForm
from django.http import HttpResponse


class ProductView(View):

    def get(self, request):
        return render(request, 'product/index.html')


class ProductRegistrationView(View):
    def get(self, request):
        return render(request, 'registration/product/index.html')

    def post(self, request):
        form = ProductRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            image1 = form.cleaned_data.get('image1')
            image2 = form.cleaned_data.get('image2')
            image3 = form.cleaned_data.get('image3')

            instance = form.instance

            for img in (image1, image2, image3):
                if not img:
                    continue
                product_image = models.ProductImage(product=instance, image=img)
                product_image.save()

                instance.product_images.add(product_image)

            print(image1)
            return redirect('/product/')

        print(request.POST)
        return HttpResponse(form.errors)
