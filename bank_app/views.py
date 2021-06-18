from django.shortcuts import render, get_object_or_404, redirect
from .models import Account, Ledger, Customer, ExternalLedger
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from forex_python.converter import CurrencyRates
import uuid
import json
from django.http import Http404
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from .serializers import ExternalLedgerSerializer, LedgerSerializer
from rest_framework.decorators import api_view
import requests
from requests.auth import HTTPBasicAuth
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from django.template.loader import get_template
from xhtml2pdf import pisa
from .utils import is_bank_employee


@login_required
def index(request):
    assert not is_bank_employee(
        request.user), 'Employee tries accessing customer view.'
    customers = Customer.objects.filter(user=request.user)
    print(customers)
    loans = Account.objects.filter(
        user=request.user).filter(account_type='LOAN')
    accounts = Account.objects.filter(
        user=request.user).filter(account_type='BANK_ACCOUNT')
    context = {
        'customers': customers,
        'accounts': accounts,
        'loans': loans
    }
    print(loans, accounts)
    return render(request, 'bank_app/index.html', context)

@login_required
def conversion(request):
    context = {}
    if request.method == 'POST':
        currency_from = request.POST['currency_from']
        currency_to = request.POST['currency_to']
        amount = float(request.POST['amount'])
        accounts = Account.objects.filter(
            user=request.user).filter(account_type='BANK_ACCOUNT')
        c = CurrencyRates()
        conversion = c.convert(currency_from, currency_to, amount)
        context = {
            'inputamount': amount,
            'currency_from': currency_from,
            'currency_to': currency_to,
            'conversion': conversion,
            'accounts': accounts

        }

        # return redirect('bank_app:index')
    return render(request, 'bank_app/conversion.html', context)


def employee(request):
    assert is_bank_employee(
        request.user), 'Customer tries accessing employee view.'
    customers = Customer.objects.all()
    accounts = Account.objects.all()
    context = {
        'customers': customers,
        'accounts': accounts
    }
    return render(request, 'bank_app/employee.html', context)


def change_rank(request, customer_id):
    assert is_bank_employee(
        request.user), 'Customer tries accessing employee view.'
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {'customer': customer}

    if request.method == 'POST':
        user = customer.user
        customer.rank = request.POST['rank']
        customer.save()
        user.save()
        return redirect('bank_app:employee')

    return render(request, 'bank_app/employee.html', context)


def add_customer(request):
    assert is_bank_employee(
        request.user), 'Customer tries accessing employee view.'
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
        user = User.objects.create_user(
            email=email, username=username, password=password, first_name=first_name, last_name=last_name)
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
    assert is_bank_employee(
        request.user), 'Customer tries accessing employee view.'
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
    assert not is_bank_employee(
        request.user), 'Employee tries accessing customer view.'
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
    assert not is_bank_employee(
        request.user), 'Employee tries accessing customer view.'
    movements = Ledger.objects.filter(id_account_fk=account_id)
    print(account_id)
    print(movements)
    context = {
        'movements': movements,
        "account_id": account_id
    }
    return render(request, 'bank_app/movements.html', context)


@login_required
def take_loan(request, customer_id):
    assert not is_bank_employee(
        request.user), 'Employee tries accessing customer view.'
    accounts = Account.objects.filter(
        user=request.user).filter(account_type='BANK_ACCOUNT')
    customer = get_object_or_404(Customer, pk=customer_id)
    context = {
        'accounts': accounts,
        'customer': customer
    }
    if request.method == 'POST':
        account_type = request.POST['account_type']
        loan_name = request.POST['loan_name']
        loan_amount = request.POST['loan_amount']
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
    assert not is_bank_employee(
        request.user), 'Employee tries accessing customer view.'
    loan = get_object_or_404(Account, pk=loan_id)
    customer = get_object_or_404(Customer, pk=customer_id)
    accounts = Account.objects.filter(
        user=request.user).filter(account_type='BANK_ACCOUNT')
    context = {
        'accounts': accounts,
        'customer': customer,
        'loan': loan
    }

    if request.method == 'POST':
        account = request.POST['account']
        amount = request.POST['amount']
        text = 'loan payment'
        selectedAccount = get_object_or_404(Account, pk=account)
        balance = selectedAccount.balance

        if balance >= int(amount) and int(amount) <= -loan.balance:
            Ledger.transaction(int(amount), account, loan.pk, text)
            if loan.balance == 0:
                loan.delete()

            return redirect('bank_app:index')
        elif int(amount) > -loan.balance:
            context = {
                'customer': customer,
                'accounts': accounts,
                'loan': loan,
                'error': 'your loan in smaller than the amount you are sending'
            }
        else:
            context = {
                'customer': customer,
                'accounts': accounts,
                'loan': loan,
                'error': 'insufficient funds'
            }

    return render(request, 'bank_app/pay_loan.html', context)


@login_required
def transfers(request, account_id):
    assert not is_bank_employee(
        request.user), 'Employee tries accessing customer view.'
    currentAccount = get_object_or_404(Account, pk=account_id)
    # currentAccount = Account.objects.filter(pk=account_id)
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
        # acc_balance = 1000
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


@login_required
def external_transfers(request, account_id):
    assert not is_bank_employee(
        request.user), 'Employee tries accessing customer view.'
    currentAccount = get_object_or_404(Account, pk=account_id)
    # currentAccount = Account.objects.filter(pk=account_id)
    allAccounts = Account.objects.exclude(pk=account_id)
    context = {
        'currentAccount': currentAccount,
        'allAccounts': allAccounts
    }
    if request.method == 'POST':

        amount = request.POST['amount']
        from_account = request.POST['fromAccount']
        to_account = request.POST['toForeignBankAccount']
        text = request.POST['text']
        acc_balance = currentAccount.balance
        foreign_account = request.POST['toAccount']

        externalLedger = ExternalLedger()
        from_account_obj = get_object_or_404(Account, pk=from_account)
        externalLedger.localAccount = from_account_obj
        externalLedger.foreignAccount = foreign_account
        externalLedger.amount = amount
        externalLedger.text = text
        transaction_id = uuid.uuid4()

        url = 'http://0.0.0.0:8003/accounts/profile/api/v1/rest-auth/login/'
        pload = {"username": "external_transfers", "password": 'external123'}
        r = requests.post(url, data=pload)
        keystring = json.loads(r.text)
        key = keystring["key"]
        print(f'Token {key}')

        # headers = {
        #     'Authorization': 'Token 4e3e5662799e6442075ccf23b8435547b8c58f15'}
        # r = requests.get(url, headers=headers)

        pload = {"localAccount": foreign_account, "foreignAccount": from_account,
                 "amount": amount, "text": text}

        my_headers = {
            'Authorization': f'Token {key}'}
        r = requests.post(
            'http://0.0.0.0:8003/accounts/profile/api/v1/external_ledger/', headers=my_headers, data=pload)
        print(r.text)

        pload = {"id_account_fk": from_account,
                 "amount": amount, "text": text, "transaction_id": transaction_id}

        my_headers = {
            'Authorization': f'Token {key}'}
        r = requests.post(
            'http://0.0.0.0:8003/accounts/profile/api/v1/ledger/', headers=my_headers, data=pload)
        print(r.text)

        # "id_account_fk": the id of the FOREIGN ACC in the other bank
        pload = {"id_account_fk": 1,
                 "amount": amount, "text": text, "transaction_id": transaction_id}

        my_headers = {
            'Authorization': f'Token {key}'}
        r = requests.post(
            'http://0.0.0.0:8003/accounts/profile/api/v1/ledger/', headers=my_headers, data=pload)
        print(r.text)

        if acc_balance >= int(amount):
            Ledger.transaction(int(amount), from_account, to_account, text)
            externalLedger.save()
            return redirect('bank_app:index')
        else:
            context = {
                'currentAccount': currentAccount,
                'allAccounts': allAccounts,
                'error': 'your balance is too low'
            }

    return render(request, 'bank_app/transfers.html', context)


@api_view(['POST'])
def api_transfers(request):
    external_ledger_serializer = ExternalLedgerSerializer(
        data=request.data, many=True)
    ledger_serializer = LedgerSerializer(
        data=request.data, many=True)
    # print(request.auth)

    if external_ledger_serializer.is_valid():
        external_ledger_serializer.save()
        return JsonResponse(external_ledger_serializer.data, status=status.HTTP_201_CREATED)
    elif ledger_serializer.is_valid():
        ledger_serializer.save()
        return JsonResponse(ledger_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(ledger_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@login_required
def pdf(request, account_id):
    movements = Ledger.objects.filter(id_account_fk=account_id)

    template_path = 'bank_app/movements_to_pdf.html'
    context = {'movements': movements, "account_id": account_id}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
