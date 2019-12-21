from rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from sample.models import *

class AddressSerializer(ModelSerializer):
    class Meta:
        model=Address
        fields='__all__'

class CustomerSerializer(ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'