from django.contrib import admin
from django.urls import path,include

from .user.views import LandingPage

urlpatterns = [
    path('', LandingPage.as_view(),name="landingpage"),
    path('admin/', admin.site.urls),
    path('customer/', include('backend.user.urls', namespace='user')),
]
