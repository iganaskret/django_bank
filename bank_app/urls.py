from django.contrib import admin
from django.urls import path, include

from . import views
from .api import CustomerList, CustomerDetail

app_name = 'bank_app'
urlpatterns = [
   path('', views.index, name='index'),
   path('pay_loan/<customer_id>/<loan_id>', views.pay_loan, name='pay_loan'),
   path('employee', views.employee, name='employee'),
   path('take_loan/<customer_id>', views.take_loan, name='take_loan'),
   path('add_account', views.add_account, name='add_account'),
   path('add_account_by_employee/', views.add_account_by_employee, name='add_account_by_employee'),
   path('add_customer/', views.add_customer, name='add_customer'),
   path('change_rank/<customer_id>', views.change_rank, name='change_rank'),
   path('transfers/<account_id>/', views.transfers, name='transfers'),
   path('movements/<account_id>/', views.movements, name='movements'),
   path('api/v1/', CustomerList.as_view()),
   path('api/v1/<int:pk>/', CustomerDetail.as_view()),
   path('api/v1/rest-auth/', include('rest_auth.urls')),

]
