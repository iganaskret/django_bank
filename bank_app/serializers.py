"""bank_app serializers"""
from rest_framework import serializers
from .models import Account, Customer, Ledger, ExternalLedger


class AccountSerializer(serializers.ModelSerializer):
    """create serializer for Account model"""
    class Meta:
        fields = ('__all__')
        #lookup_field = 'account_number'
        extra_kwargs = {
            'url': {'lookup_field': 'account_number'}}
        model = Account


class LedgerSerializer(serializers.ModelSerializer):
    """create serializer for Ledger model"""
    class Meta:
        model = Ledger
        fields = ('__all__')


class ExternalLedgerSerializer(serializers.ModelSerializer):
    """create serializer for External Ledger model"""
    class Meta:
        model = ExternalLedger
        fields = ('__all__')


class CustomerSerializer(serializers.ModelSerializer):
    """convert customer object"""
    #first_name = serializers.CharField(source='Customer.first_name')
    class Meta:
        model = Customer
        fields = ('__all__')
