from django.shortcuts import render
from .models import Account


def index(request):
   customer = Account.objects.all()
   context = {
      'customer': customer
   }
   return render(request, 'bank_app/index.html', context)

