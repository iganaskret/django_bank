from rest_framework import serializers
from .models import Account
from .models import Ledger
from django.db import transaction


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Ledger

    @transaction.atomic
    def create(self, instance, validated_data):
        # def transaction(cls, amount, from_account, to_account, text):
        instance.id = uuid.uuid4()
        instance.id_account_fk = validated_data.get(
            "fromAccount", instance.id_account_fk)
        instance.amount = validated_data.get("amount", instance.amount)
        instance.text = validated_data.get("text", instance.text)
        instance.save()
        # ledger = Ledger()
        # ledger = cls(id_account_fk=id_account_fk, amount=-
        # amount, text = text, transaction_id = id)
        return super(LedgerSerializer, self).create(instance)


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('__all__')
        model = Account
