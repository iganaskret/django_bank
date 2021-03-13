from django.contrib import admin
from django.urls import path

from . import views


app_name = 'bank_app'
urlpatterns = [
   path('', views.index, name='index'),
   path('take_loan', views.take_loan, name='take_loan'),
   path('add_account', views.add_account, name='add_account'),
   path('movements/<account_id>/', views.movements, name='movements')
]
