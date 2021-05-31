from django.contrib import admin
from .models import Customer
from .models import Account
from .models import Ledger
from .models import ExternalLedger

admin.site.register(Customer)
admin.site.register(Ledger)
admin.site.register(Account)
admin.site.register(ExternalLedger)

# Register your models here.
