"""api configuration"""
from rest_framework import generics
from .models import Account, Ledger, ExternalLedger
from .serializers import AccountSerializer, LedgerSerializer, ExternalLedgerSerializer
from .utils import is_bank_employee
from .permissions import IsOwnerOrNoAccess


class AccountList(generics.ListCreateAPIView):
    """collection of account instances"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        if is_bank_employee(self.request.user):
            queryset = Account.objects.all()
            return queryset
        else:
            queryset = Account.objects.filter(user=self.request.user)
            return queryset


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    """read-write-delete endpoints to represent an account instance"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'account_number'


class LedgerList(generics.ListCreateAPIView):
    """collection of ledger instances"""
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

    def get_queryset(self):
        if is_bank_employee(self.request.user):
            queryset = Ledger.objects.all()
            return queryset


class ExternalLedgerList(generics.ListCreateAPIView):
    """collection of external ledger instances"""
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer

    def get_queryset(self):
        if is_bank_employee(self.request.user):
            queryset = ExternalLedger.objects.all()
            return queryset


class LedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    """read-write-delete endpoints to represent ledger instance"""
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class ExternalLedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    """read-write-delete endpoints to represent external ledger instance"""
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer
