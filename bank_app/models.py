from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.db.models import Sum

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    class Rank(models.TextChoices):
        BASIC = 'Basic'
        SILVER = 'Silver'
        GOLD = 'Gold'
    rank = models.CharField(choices=Rank.choices, default=Rank.BASIC, max_length=200)
    phone_number=models.CharField(max_length=20)
    @property
    def can_make_loan(self):
        if self.rank == 'Basic':
            return False
        else:
            return True
    def __str__(self):
        return f"{self.user.first_name} - {self.user.id} - {self.rank}"


class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    account_number=models.CharField(max_length=10)

    class AccountType(models.TextChoices):
        BANK_ACCOUNT = 'Bank Account'
        LOAN = 'Loan'

    account_type = models.CharField(choices=AccountType.choices, default=AccountType.BANK_ACCOUNT, max_length=200)
    name=models.CharField(max_length=20)
    @property
    def balance(self):
        ledger_sum = Ledger.objects.filter(id_account_fk=self.id).aggregate(Sum('amount'))
        for key, value in ledger_sum.items():
            return  value

    def __str__(self):
        return f"{self.name} - {self.id} - {self.user.id} - {self.balance}"

class Ledger(models.Model):
   #transaction_id
   id_account_fk=models.ForeignKey('Account',on_delete=models.CASCADE, related_name="ledger")
   amount=models.DecimalField(max_digits=20, decimal_places=2)
   text=models.CharField(max_length=20)
   date_created=models.DateTimeField(auto_now_add=True)
  # @property
  # def total_amount(self):
    #   calc=Ledger.objects.annotate(total_amount=Sum('amount'))
   #    return self.calc
   def __str__(self):
       return f"{self.id_account_fk} - {self.amount}"
