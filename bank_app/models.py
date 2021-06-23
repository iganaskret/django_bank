"""bank_app models"""
import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db import transaction
from django.shortcuts import get_object_or_404


class Customer(models.Model):
    """customer database fields"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True,)

    class Rank(models.TextChoices):
        """customer rank choices"""
        BASIC = 'Basic'
        SILVER = 'Silver'
        GOLD = 'Gold'
    rank = models.CharField(choices=Rank.choices,
                            default=Rank.BASIC, max_length=200)
    phone_number = models.CharField(max_length=20)

    @property
    def can_make_loan(self):
        """condition - basic rank can't take a loan"""
        if self.rank == 'Basic':
            return False

        return True

    def __str__(self):
        return f"{self.user.first_name} - {self.user.id} - {self.rank}"


class Account(models.Model):
    """customer account fields"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="account")
    account_number = models.CharField(max_length=10)

    class AccountType(models.TextChoices):
        """account type fields"""
        BANK_ACCOUNT = 'Bank Account'
        LOAN = 'Loan'
        FOREIGN_BANK_ACCOUNT = 'Foreign Bank Account '

    account_type = models.CharField(
        choices=AccountType.choices, default=AccountType.BANK_ACCOUNT, max_length=200)
    name = models.CharField(max_length=20)

    @property
    def balance(self):
        """function - sum of the ledger"""
        ledger_sum = Ledger.objects.filter(
            account=self.id).aggregate(Sum('amount'))
        external_ledger_sum = ExternalLedger.objects.filter(
            localAccount=self.id).aggregate(Sum('amount'))

        for key, value in ledger_sum.items():
            if value is None:
                balance = 0
            else:
                balance = value

        for key, value in external_ledger_sum.items():
            if value is None:
                external_balance = 0
            else:
                external_balance = value

        return balance + external_balance

    def __str__(self):
        return f"{self.name} - {self.id} - {self.user.id} - {self.balance}"


class Ledger(models.Model):
    """ledger fields"""
    account = models.ForeignKey(
        'Account', on_delete=models.CASCADE, related_name="ledger")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    text = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.account.id} - {self.amount} -  {self.text} - {self.transaction_id}"

    @classmethod
    @transaction.atomic
    def transaction(cls, amount, from_account, to_account, text):
        """function - atomic transaction save"""
        id_ = uuid.uuid4()
        sender_account = get_object_or_404(Account, pk=from_account)
        ledger = Ledger()
        ledger = cls(account=sender_account, amount=-
                     amount, text=text, transaction_id=id_)
        ledger.save()
        receiver_account = get_object_or_404(Account, pk=to_account)
        ledger = Ledger()
        ledger = cls(account=receiver_account,
                     amount=amount, text=text, transaction_id=id_)
        ledger.save()


class ExternalLedger(models.Model):
    """external ledger fields"""
    localAccount = models.ForeignKey(
        'Account', on_delete=models.CASCADE, related_name="external_ledger")
    foreignAccount = models.CharField(max_length=100, blank=False)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    text = models.CharField(max_length=100)
    comments = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.localAccount.name} - {self.foreignAccount} -  {self.amount} -  {self.text}"
