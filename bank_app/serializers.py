from rest_framework import serializers
from .models import Account
from .models import Ledger
from .models import ExternalLedger
from django.db import transaction
from django.shortcuts import get_object_or_404
import uuid


class AccountSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('__all__')
        lookup_field = 'account_number'
        extra_kwargs = {"pk": {"read_only": False},
                        'url': {'lookup_field': 'account_number'}}
        model = Account


class LedgerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ledger
        fields = ('account', 'amount', 'text', 'transaction_id')
        extra_kwargs = {"pk": {"read_only": False}}


class ExternalLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalLedger
        fields = ('__all__')
        extra_kwargs = {"pk": {"read_only": False}}
