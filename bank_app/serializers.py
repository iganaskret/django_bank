"""bank_app serializers"""
from rest_framework import serializers
from .models import Account, Ledger, ExternalLedger


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        #lookup_field = 'account_number'
        extra_kwargs = {
            'url': {'lookup_field': 'account_number'}}
        model = Account


class LedgerSerializer(serializers.ModelSerializer):
    """convert ledger object"""
    class Meta:
        model = Ledger
        fields = ('__all__')


class ExternalLedgerSerializer(serializers.ModelSerializer):
    """convert external ledger object"""
    class Meta:
        model = ExternalLedger
        fields = ('__all__')
