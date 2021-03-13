from django.shortcuts import render, redirect
from .models import Account, Ledger, Customer
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
   customers = Customer.objects.filter(user=request.user)
   print(customers)
   loans= Account.objects.filter(user=request.user).filter(account_type='LOAN')
   accounts = Account.objects.filter(user=request.user).filter(account_type= 'BANK_ACCOUNT')
#   accounts = Account.objects.filter(user=request.user)
   context = {
      'customers': customers,
      'accounts': accounts,
      'loans': loans
   }
   print( loans, accounts)
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

@login_required
def movements(request, account_id):
    movements = Ledger.objects.filter(id_account_fk=account_id)
    print(movements)
    context = {
            'movements': movements
    }
    return render(request, 'bank_app/movements.html', context)

@login_required
def take_loan(request):
    accounts = Account.objects.filter(user=request.user)
    customers = Customer.objects.filter(user=request.user)
    context = {
            'accounts': accounts
    }
    if request.method == 'POST':
        account_type = request.POST['account_type']
        loan_name = request.POST['loan_name']
        loans_amount = request.POST['loan_amount']
        account = Account()
        account.user = request.user
        account.name = loan_name
        account.account_number = "12345678"
        account.account_type = account_type
        account.save()

        return redirect('bank_app:index')

    return render(request, 'bank_app/take_loan.html', context)
