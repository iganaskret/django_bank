from django.shortcuts import render
from .models import Account, Ledger, Customer


def index(request):
   customers = Customer.objects.all()
   accounts = Account.objects.all()
   context = {
      'customers': customers,
      'accounts': accounts
   }
   return render(request, 'bank_app/index.html', context)

