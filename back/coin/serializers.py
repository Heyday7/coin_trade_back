from .models import Coin, CoinHolding, CoinPrice
from rest_framework import serializers


class CoinPriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoinPrice
        fields = '__all__'


class CoinHoldingSerializer(serializers.ModelSerializer):
    type = serializers.CharField(write_only=True)
    class Meta:
        model = CoinHolding
        fields = '__all__'


    def validate(self, data):
        if data['type'] == 'sell' and not self.instance:
            raise serializers.ValidationError('!!1 오류')
        elif data['type'] == 'sell' and self.instance:
            if self.instance.coin_amount < data['coin_amount']:
                raise serializers.ValidationError('11111')
        
        return data

    def create(self, validated_data):
        type = validated_data.pop('type')
        coinHolding = CoinHolding.objects.create(**validated_data)
        account = validated_data['account']
        account.balance -= validated_data['total_price']
        account.save()

        return coinHolding

    def update(self, instance, validated_data):
        type = validated_data.pop('type')
        account = validated_data['account']

        if type == 'buy':
            instance.coin_amount += validated_data['coin_amount']
            instance.total_price += validated_data['total_price']
            instance.price = instance.total_price / instance.coin_amount 
            account.balance -= validated_data['total_price']
        
        elif type == 'sell':
            instance.coin_amount -= validated_data['coin_amount']
            instance.total_price = instance.coin_amount * instance.price

            account.balance += validated_data['total_price']

        if instance.coin_amount == 0:
            instance.delete()
        else:
            instance.save()
        account.save()

        return instance