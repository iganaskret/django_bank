from django.shortcuts import render, redirect
from .models import Account, Ledger, Customer
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
   customers = Customer.objects.filter(user=request.user)
   accounts = Account.objects.filter(user=request.user)
   context = {
      'customers': customers,
      'accounts': accounts
   }
   return render(request, 'bank_app/index.html', context)

@login_required
def add_account(request):
    accounts = Account.objects.filter(user=request.user)
    customers = Customer.objects.filter(user=request.user)
    context = {
            'accounts': accounts
    }
    if request.method == 'POST':
        account_type = request.POST['account_type']
        account_name = request.POST['name']
        account = Account()
        account.user = request.user
        account.name = account_name
        account.account_number = "12345678"
        account.account_type = account_type
        account.save()

        return redirect('bank_app:index')

    return render(request, 'bank_app/add_account.html', context)

