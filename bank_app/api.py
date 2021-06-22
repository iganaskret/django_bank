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
from .utils import is_bank_employee
from .permissions import IsOwnerOrNoAccess


class AccountList(generics.ListCreateAPIView):
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
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'account_number'

    # def get_queryset(self):
    #     if is_bank_employee(self.request.user):
    #         queryset = Account.objects.all()
    #         return queryset
    #     else:
    #         queryset = Account.objects.filter(user=self.request.user)
    #         return queryset


class LedgerList(generics.ListCreateAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

    def get_queryset(self):
        if is_bank_employee(self.request.user):
            queryset = Ledger.objects.all()
            return queryset


class ExternalLedgerList(generics.ListCreateAPIView):
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer

    def get_queryset(self):
        if is_bank_employee(self.request.user):
            queryset = ExternalLedger.objects.all()
            return queryset


class LedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ledger.objects.all()
    serializer_class = LedgerSerializer

    # def get_queryset(self):
    #     if is_bank_employee(self.request.user):
    #         queryset = Ledger.objects.all()
    #         return queryset


class ExternalLedgerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ExternalLedger.objects.all()
    serializer_class = ExternalLedgerSerializer

    # def get_queryset(self):
    #     if is_bank_employee(self.request.user):
    #         queryset = ExternalLedger.objects.all()
    #         return queryset
