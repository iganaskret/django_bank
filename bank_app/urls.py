from django.contrib import admin
from django.urls import path, include
#from rest_framework.authtoken import views

from . import views
from .api import AccountList, AccountDetail, LedgerList, LedgerDetail, ExternalLedgerList, ExternalLedgerDetail

app_name = 'bank_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('conversion/<account_id>/', views.conversion, name='conversion'),
    path('pay_loan/<customer_id>/<loan_id>', views.pay_loan, name='pay_loan'),
    path('employee', views.employee, name='employee'),
    path('take_loan/<customer_id>', views.take_loan, name='take_loan'),
    path('add_account', views.add_account, name='add_account'),
    path('add_account_by_employee/', views.add_account_by_employee,
         name='add_account_by_employee'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('change_rank/<customer_id>', views.change_rank, name='change_rank'),
    path('transfers/<account_id>/', views.transfers, name='transfers'),
    path('external_transfers/<account_id>/',
         views.external_transfers, name='external_transfers'),
    path('movements/<account_id>/', views.movements, name='movements'),
    path('pdf/<account_id>/', views.pdf, name='pdf'),
    path('api/v1/accounts/', AccountList.as_view()),
    path('api/v1/accounts/<account_number>/', AccountDetail.as_view()),
    path('api/v1/ledger/', LedgerList.as_view()),
    path('api/v1/external_ledger/', ExternalLedgerList.as_view()),
    path('api/v1/ledger/<int:pk>/', LedgerDetail.as_view()),
    path('api/v1/external_ledger/<int:pk>/', ExternalLedgerDetail.as_view()),
    path('api/v1/rest-auth/', include('rest_auth.urls')),
]
