from django.contrib import admin
from .models import Customer
from .models import Transaction

# Register your models here.

admin.site.register(Customer)
admin.site.register(Transaction)
