"""bank_app urlpatterns"""
from django.urls import path, include
from . import views
from .api import AccountList, LedgerList, ExternalLedgerList, CustomerList
from .api import AccountDetail, LedgerDetail, ExternalLedgerDetail, CustomerListDetail


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

    path('api/v1/', include([
         path('accounts/', AccountList.as_view()),
         path('accounts/<account_number>/', AccountDetail.as_view()),
         path('ledger/', LedgerList.as_view()),
         path('external_ledger/', ExternalLedgerList.as_view()),
         path('ledger/<int:pk>/', LedgerDetail.as_view()),
         path('external_ledger/<int:pk>/', ExternalLedgerDetail.as_view()),

         path('customers/', CustomerList.as_view()),
         path('customers/<int:pk>/', CustomerListDetail.as_view()),

         path('rest-auth/', include('rest_auth.urls')),
         ])),
]
