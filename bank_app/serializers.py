from rest_framework import serializers
from django.shortcuts import render, get_object_or_404, redirect


from .models import Customer, Account, Ledger


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('user', 'account_number',
                  'account_type', 'name', 'balance', 'id')


class LedgerSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = Ledger
        fields = ('id_account_fk', 'amount', 'text', 'id')

    def create(self, validated_data):

        # user = self.context['request'].user
        # validated_data['user'] = user

        account = get_object_or_404(Account, pk=account_id)
        validated_data['account'] = account

        return super(LedgerSerializer, self).create(validated_data)
