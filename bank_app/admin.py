"""display bank_app models in the admin panel"""
from django.contrib import admin
from .models import Customer, Account, Ledger, ExternalLedger

admin.site.register(Customer)
admin.site.register(Ledger)
admin.site.register(Account)
admin.site.register(ExternalLedger)
