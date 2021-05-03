from rest_framework import serializers
from .models import Ledger


class LedgerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id_account_fk', 'amount', 'text',
                  'date_created', 'transaction_id')
        model = Ledger
