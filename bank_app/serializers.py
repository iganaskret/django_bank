from rest_framework import serializers
from .models import Account
from .models import Ledger


class LedgerSerializer(serializers.ModelSerializer):
   class Meta:
      fields = ('__all__')
      model = Ledger


class AccountSerializer(serializers.ModelSerializer):
   class Meta:
      fields = ('__all__')
      model = Account