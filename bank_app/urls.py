from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views


app_name = 'bank_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('pay_loan/<customer_id>/<loan_id>', views.pay_loan, name='pay_loan'),
    path('employee', views.employee, name='employee'),
    path('take_loan/<customer_id>', views.take_loan, name='take_loan'),
    path('add_account', views.add_account, name='add_account'),
    path('add_account_by_employee/', views.add_account_by_employee,
         name='add_account_by_employee'),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('change_rank/<customer_id>', views.change_rank, name='change_rank'),
    path('transfers/<account_id>/', views.transfers, name='transfers'),
    path('movements/<account_id>/', views.movements, name='movements'),
    # chat
    path('chat/', include('chat_app.urls'))
]
