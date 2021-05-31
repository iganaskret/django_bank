from rest_framework import generics
# from rest_framework import permissions
from rest_framework.response import Response
from .models import Account, Ledger, ExternalLedger
from .serializers import AccountSerializer, LedgerSerializer, ExternalLedgerSerializer
from django.shortcuts import get_object_or_404, redirect
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
import json

# from .permissions import IsOwnerOrNoAccess


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# class LedgerList(generics.ListCreateAPIView):
#     queryset = Ledger.objects.all()
#     serializer_class = LedgerSerializer

#     def post(self, request, *args, **kwargs):

#         request.data._mutable = True
#         # request.data['id_account_fk'] = request.POST['fromAccount']
#       #   post = request.POST.copy()
#         from_account = request.POST['fromAccount']
#         request.data._mutable = False
#       #   request.POST['id_account_fk'] = request.POST['fromAccount']
#       #   request.POST = post
#       #   request.data.update({"id_account_fk": request.POST['fromAccount']})
#         account = get_object_or_404(Account, pk=from_account)
#         amount = request.data['amount']
#         text = request.data['text']

#         serializer = LedgerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         #   ledger1 = Ledger.objects.create(
#       #        id_account_fk=account, amount=amount, text=text, transaction_id=1)
#       #   ledger = {"id_account_fk": {"id": account.id,
#       #                                 "account_number": account.account_number,
#       #                                 "account_type": account.account_type,
#       #                                   "name": account.name,
#       #                                   "user": account.user.pk}, "amount": amount,
#       #               "text": text, "transaction_id": 1}
#         # data = JSONParser().parse(ledger1)
#         # l(id_account_fk=validated_data.get("id_account_fk"), amount=validated_data.get(
#         #     "amount"), text=validated_data.get("text"), transaction_id=transaction_id)


class LedgerList(generics.ListCreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class ExternalLedgerList(generics.ListCreateAPIView):
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer


class LedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer


class ExternalLedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer
