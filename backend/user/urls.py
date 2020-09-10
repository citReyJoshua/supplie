from django.urls import path
from . import views

app_name='user'

urlpatterns = [
    path('', views.CustomerView.as_view(), name='index'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='registration')
]
