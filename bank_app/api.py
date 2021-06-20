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

from .permissions import IsOwnerOrNoAccess


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'account_number'


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
