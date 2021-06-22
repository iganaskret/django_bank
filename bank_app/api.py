"""api configuration"""
from rest_framework import generics
from .models import Account, Ledger, ExternalLedger, Customer
from .serializers import AccountSerializer, LedgerSerializer, ExternalLedgerSerializer, CustomerSerializer
from .permissions import IsOwnerOrNoAccess


class AccountList(generics.ListCreateAPIView):
    """collection of account instances"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    """read-write-delete endpoints to represent an account instance"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'account_number'


class LedgerList(generics.ListCreateAPIView):
    """collection of ledger instances"""
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class ExternalLedgerList(generics.ListCreateAPIView):
    """collection of external ledger instances"""
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer


class LedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    """read-write-delete endpoints to represent ledger instance"""
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class ExternalLedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    """read-write-delete endpoints to represent external ledger instance"""
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer


#
class CustomerList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.filter(user=self.request.user)
        return queryset


class CustomerListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
