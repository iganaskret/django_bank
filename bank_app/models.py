from django.db import models
from django.contrib.auth.models import User
#class Customers(models.Model):
 #   first_name=models.CharField(max_length=30)
  #  last_name=models.CharField(max_length=30)
   # completed=models.BooleanField(default=False)
   # created=models.DateTimeField(auto_now_add=True)
   # def __str__(self):
    #    return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    rank=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.user.first_name}"

class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=10)
    #balance=models.DecimalField(max_digits=20, decimal_places=2)
    isLoan=models.BooleanField(default=False)
    name=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.user}"

#class Ledger(models.Model):
   # transaction_id
   #id_account_fk=models.ForeignKey('Account_info',on_delete=models.CASCADE)
   #amount=models.DecimalField(max_digits=20, decimal_places=2)
   #currency=models.CharField(max_length=3)
   #date_created=models.DateTimeField(auto_now_add=True)

