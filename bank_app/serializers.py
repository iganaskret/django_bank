from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('user', 'rank', 'phone_number')
