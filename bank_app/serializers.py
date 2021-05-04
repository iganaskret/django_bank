from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
   class Meta:
      fields = ('user', 'rank', 'phone_number')
      model = Customer
