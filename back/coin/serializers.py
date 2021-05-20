from .models import Coin
from rest_framework import serializers


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = '__all__'

