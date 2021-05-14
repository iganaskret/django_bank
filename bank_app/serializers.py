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
        extra_kwargs = {"pk": {"read_only": False}}
        model = Account

# class LedgerSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ('__all__')
#         model = Ledger

#     @transaction.atomic
#     def create(self, instance, validated_data):
#         # def transaction(cls, amount, from_account, to_account, text):
#         instance.id = uuid.uuid4()
#         instance.id_account_fk = validated_data.get(
#             "fromAccount", instance.id_account_fk)
#         instance.amount = validated_data.get("amount", instance.amount)
#         instance.text = validated_data.get("text", instance.text)
#         instance.save()
#         # ledger = Ledger()
#         # ledger = cls(id_account_fk=id_account_fk, amount=-
#         # amount, text = text, transaction_id = id)
#         return super(LedgerSerializer, self).create(instance)


class LedgerSerializer(serializers.ModelSerializer):
    #id_account_fk = AccountSerializer()

    class Meta:
        model = Ledger
        fields = ('id_account_fk', 'amount', 'text')
        extra_kwargs = {"pk": {"read_only": False}}

    # def create(self, validated_data):
    #     print(validated_data)
    #     account_data = validated_data.pop('id_account_fk')
    #     print(account_data)
    #     account = get_object_or_404(Account, pk=validated_data.get("text"))
    #     #account = Account.objects.create(**account_data)
    #     ledger = Ledger.objects.create(id_account_fk=account, **validated_data)
    #     return ledger

    # @transaction.atomic
    # def create(self, instance, validated_data):
    #     # def transaction(cls, amount, from_account, to_account, text):
    #     instance.id = uuid.uuid4()
    #     instance.id_account_fk = validated_data.get(
    #         "id_account_fk", instance.id_account_fk)
    #     instance.amount = validated_data.get("amount", instance.amount)
    #     instance.text = validated_data.get("text", instance.text)
    #     instance.save()
    #     # ledger = Ledger()
    #     # ledger = cls(id_account_fk=id_account_fk, amount=-
    #     # amount, text = text, transaction_id = id)
    #     return super(LedgerSerializer, self).create(instance)
        # extra_kwargs = {'id_account_fk': {'required': False}}

    # def is_valid(self, raise_exception=False):
    #     is_validated = super().is_valid(raise_exception=False)

    # new comment def create(self, validated_data):

        #     # user = self.context['request'].user
        #     # validated_data['user'] = user
        # new comment transaction_id = uuid.uuid4()
        # account = get_object_or_404(
        #     Account, pk=validated_data.get("fromAccount"))
        # ledger = Ledger.objects.create(id_account_fk=validated_data.get("id_account_fk"), amount=validated_data.get(
        #     "amount"), text=validated_data.get("text"), transaction_id=transaction_id)
        # new comment ledger = Ledger.objects.create(**validated_data)
        # new comment return ledger

        #     #account_data = validated_data.pop('account')
        #     id_account_fk = get_object_or_404(
        #         Account, iban=account_data['iban'], users__pk=user.id)
        #     validated_data['account'] = account

        #     currency_data = validated_data.pop('currency')
        #     currency = get_object_or_404(Currency, code=currency_data['code'])
        #     validated_data['currency'] = currency

        #     validated_data['amount_bgn'] = round(
        #         validated_data['amount'] * currency.rate_to_bgn, 2)

        #     return super(FundTransferSerializer, self).create(validated_data)


class ExternalLedgerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalLedger
        fields = ('__all__')
        extra_kwargs = {"pk": {"read_only": False}}
