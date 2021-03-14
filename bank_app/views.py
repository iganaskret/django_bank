from django.shortcuts import render, get_object_or_404, redirect
from .models import Account, Ledger, Customer
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

@login_required
def index(request):
   customers = Customer.objects.filter(user=request.user)
   print(customers)
   loans= Account.objects.filter(user=request.user).filter(account_type='LOAN')
   accounts = Account.objects.filter(user=request.user).filter(account_type= 'BANK_ACCOUNT')
   context = {
      'customers': customers,
      'accounts': accounts,
      'loans': loans
   }
   print( loans, accounts)
   return render(request, 'bank_app/index.html', context)

def employee(request):
    customers = Customer.objects.all()
    accounts = Account.objects.all()
    context = {
            'customers': customers,
            'accounts': accounts
    }
    return render(request, 'bank_app/employee.html', context)

def change_rank(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)
    context = { 'customer': customer }

    if request.method == 'POST':
        user = customer.user
        customer.rank = request.POST['rank']
        customer.save()
        user.save()
        return redirect('bank_app:employee')

    return render(request, 'bank_app/employee.html', context)

def add_customer(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        rank = request.POST['rank']
        username = request.POST['username']
        user = User.objects.create_user(email=email, username=username, password=password, first_name=first_name, last_name=last_name)
        if password == confirm_password:
            if Customer.objects.create(user=user, phone_number=phone, rank=rank):
                return HttpResponseRedirect(reverse('bank_app:employee'))
            else:
                context = {
                        'error': 'Could not create user account - please try again.'
                }
        else:
            context = {
                    'error': 'Passwords did not match. Please try again.'
            }
    return render(request, 'bank_app/employee.html', context)

def add_account_by_employee(request):
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

         return redirect('bank_app:employee')
     return render(request, 'bank_app/employee.html', context)

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
def take_loan(request, customer_id):
    accounts = Account.objects.filter(user=request.user).filter(account_type='BANK_ACCOUNT')
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {
            'accounts': accounts,
            'customer': customer
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
        loan_amount = request.POST['loan_amount']
        from_account = account.pk
        to_account = request.POST['toAccount']
        text = "loan"
        Ledger.transaction(int(loan_amount), from_account, to_account, text)

        return redirect('bank_app:index')

    return render(request, 'bank_app/take_loan.html', context)

@login_required
def pay_loan(request, customer_id, loan_id):
    loan = get_object_or_404(Account, pk=loan_id)
    customer = get_object_or_404(Customer, pk=customer_id)
    accounts = Account.objects.filter(user=request.user).filter(account_type='BANK_ACCOUNT')
    context = {
            'accounts': accounts,
            'customer': customer,
            'loan': loan
    }

    return render(request, 'bank_app/pay_loan.html', context)


@login_required
def transfers(request, account_id):
    currentAccount = get_object_or_404(Account, pk=account_id)
    #currentAccount = Account.objects.filter(pk=account_id)
    print(currentAccount)
    allAccounts = Account.objects.exclude(pk=account_id)
    context = {
        'currentAccount': currentAccount,
        'allAccounts': allAccounts
    }
    if request.method == 'POST':
        amount = request.POST['amount']
        from_account = request.POST['fromAccount']
        to_account = request.POST['toAccount']
        text = request.POST['text']
        acc_balance = currentAccount.balance
        #acc_balance = 1000
        if acc_balance >= int(amount):
            Ledger.transaction(int(amount), from_account, to_account, text)
            return redirect('bank_app:index')
        else:
            context = {
                'currentAccount': currentAccount,
                'allAccounts': allAccounts,
                'error': 'your balance is too low'
            }

    return render(request, 'bank_app/transfers.html', context)

