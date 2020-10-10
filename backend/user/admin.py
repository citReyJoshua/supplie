from django.contrib import admin
from backend.user.models import Person, Customer, Transaction

admin.site.register(Person)
admin.site.register(Customer)
admin.site.register(Transaction)
