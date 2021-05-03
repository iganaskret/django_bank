from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Ledger, Customer, Account
from .serializers import LedgerSerializer
from .permissions import IsOwnerOrNoAccess


class LedgerList(generics.ListCreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

    # def get_queryset(self):
    #user = self.request.user
    # account = Account.objects.filter(
    #     user=self.request.user).filter(account_type='BANK_ACCOUNT')
    # queryset = Ledger.objects.filter(
    #     id_account_fk=self.request.user.account_number)
    # return queryset
    # print(accounts)

    # class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    #     queryset = Todo.objects.all()
    #     serializer_class = TodoSerializer
