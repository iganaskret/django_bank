from django.shortcuts import render
from .models import Customer


def index(request):
   customer = Customer.objects.all()
   context = {
      'customer': customer
   }
   return render(request, 'bank_app/index.html', context)

