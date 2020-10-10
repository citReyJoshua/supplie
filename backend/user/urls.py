from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.CustomerView.as_view(), name='index'),
    path('order/', views.ProductOrderView.as_view(), name='order'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='registration')
]
