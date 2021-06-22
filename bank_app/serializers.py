"""bank_app serializers"""
from rest_framework import serializers
from .models import Account, Customer, Ledger, ExternalLedger


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('__all__')
        #lookup_field = 'account_number'
        extra_kwargs = {
            'url': {'lookup_field': 'account_number'}
        }
        model = Account


class LedgerSerializer(serializers.ModelSerializer):
    """convert ledger object"""
    class Meta:
        model = Ledger
        fields = ('account', 'amount', 'text', 'transaction_id')


class ExternalLedgerSerializer(serializers.ModelSerializer):
    """convert external ledger object"""
    class Meta:
        model = ExternalLedger
        fields = ('__all__')


class CustomerSerializer(serializers.ModelSerializer):
    """convert customer object"""
    #first_name = serializers.CharField(source='Customer.first_name')

    class Meta:
        model = Customer
        fields = ('__all__')
