from django.contrib import admin
from .models import Customer
from .models import Account
from .models import Ledger

admin.site.register(Customer)
admin.site.register(Ledger)
admin.site.register(Account)

# Register your models here.
