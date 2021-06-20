"""bank_app serializers"""
from rest_framework import serializers
from .models import Account, Ledger, ExternalLedger


class AccountSerializer(serializers.ModelSerializer):
    """convert account object"""
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('__all__')
        lookup_field = 'account_number'
        extra_kwargs = {
            "pk": {"read_only": False},
            'url': {'lookup_field': 'account_number'}
        }
        model = Account


class LedgerSerializer(serializers.ModelSerializer):
    """convert ledger object"""
    class Meta:
        model = Ledger
        fields = ('id_account_fk', 'amount', 'text', 'transaction_id')
        extra_kwargs = {"pk": {"read_only": False}}


class ExternalLedgerSerializer(serializers.ModelSerializer):
    """convert external ledger object"""
    class Meta:
        model = ExternalLedger
        fields = ('__all__')
        extra_kwargs = {"pk": {"read_only": False}}
