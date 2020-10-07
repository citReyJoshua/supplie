from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from . import models
from .forms import ProductRegistrationForm
from .models import Product, ProductImage
from .choices import Category as categories, Color as colors


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()  # pylint: disable=no-member
        images = ProductImage.objects.all()  # pylint: disable=no-member

        context = {
            'products': products,
            'images': images,
            'categories': categories.choices,
            'colors': colors.choices,
        }
        return render(request, 'product/index.html', context)

    def post(self, request):
        if 'btndelete' in request.POST:
            id = request.POST.get('btndelete')
            Product.objects.get(id=id).delete()  # pylint: disable=no-member

        elif 'btnupdate' in request.POST:
            name = request.POST.get('name')
            category = request.POST.get('category')
            brand = request.POST.get('brand')
            color = request.POST.get('color')
            price = request.POST.get('price')
            no_of_stocks = request.POST.get('no_of_stocks')

            id = request.POST.get('btnupdate')
            Product.objects.filter(id=id).update(  # pylint: disable=no-member
                name=name,
                category=category,
                brand=brand,
                color=color,
                price=price,
                no_of_stocks=no_of_stocks,
            )
        return redirect('/product/#')


class ProductRegistrationView(View):

    def get(self, request):
        context = {
            'categories': categories.choices,
            'colors': colors.choices,
        }
        return render(request, 'registration/product/index.html', context)

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
                product_image = models.ProductImage(
                    product=instance, image=img)
                product_image.save()

                instance.product_images.add(product_image)

            return redirect('/product/')

        return HttpResponse(form.errors)


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()  # pylint: disable=no-member
        product_images = ProductImage.objects.all()  # pylint: disable=no-member
        context = {
            'products': products,
            'product_images': product_images
        }
        return render(request, 'buy/index.html', context)
