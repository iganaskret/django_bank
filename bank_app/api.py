from rest_framework import generics
# from rest_framework import permissions
from rest_framework.response import Response
from .models import Account, Ledger
from .serializers import AccountSerializer, LedgerSerializer
# from .permissions import IsOwnerOrNoAccess


class AccountList(generics.ListCreateAPIView):
   queryset = Account.objects.all()
   serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Account.objects.all()
   serializer_class = AccountSerializer

class LedgerList(generics.ListCreateAPIView):
   queryset = Ledger.objects.all()
   serializer_class = LedgerSerializer


class LedgerDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Ledger.objects.all()
   serializer_class = LedgerSerializer