from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerSerializer
from .permissions import IsOwnerOrNoAccess



class CustomerList(generics.ListCreateAPIView):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer
def get_queryset(self):
      queryset = Customer.objects.filter(user=self.request.user)
      return queryset

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Customer.objects.all()
   serializer_class = CustomerSerializer
