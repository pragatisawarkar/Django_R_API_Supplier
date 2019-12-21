from django.shortcuts import render
from sample.models import *
from rest_framework.viewsets import *
from sample.serializer import *
# Create your views here.

class CustomerOp(ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class AddressOp(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer