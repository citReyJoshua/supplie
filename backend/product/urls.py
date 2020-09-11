from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductView.as_view(), name='index'),
    path('registration/', views.ProductRegistrationView.as_view(), name='registration'),
]