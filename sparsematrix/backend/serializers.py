from rest_framework import serializers
from .models import *
class PinOrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model=PinOrdered
        fields=("merchantId",)
class MerchantOrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model=MerchantOrdered
        fields=("pinCode",)