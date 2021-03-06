from coin.models import CoinHolding
from coin.serializers import CoinHoldingSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Account, Transaction
from django.shortcuts import get_object_or_404


class UserSerializer(serializers.ModelSerializer):
	confirm = serializers.CharField(max_length=100, write_only=True)
	email = serializers.EmailField(required=True)

	class Meta:
		model = User
		fields = ['id', 'username', 'password', 'email', 'confirm']
	
	def validate(self, data):
		if data['password'] != data['confirm']:
			raise serializers.ValidationError('비밀번호와 비밀번호 확인이 일치하지 않습니다.')
		return data
	
	def create(self, validated_data):
		validated_data.pop('confirm')
		user = User.objects.create(**validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user

	def update(self, instance, validated_data):
		instance.username = validated_data['username']
		instance.password = validated_data['password']
		instance.email = validated_data['email']
		instance.save()


class LoginSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=100, required=True)
	password = serializers.CharField(max_length=100, required=True)

	def validate(self, data):
		user = authenticate(username=data['username'], password=data['password'])
		if not user:
			raise serializers.ValidationError("아이디 혹은 비밀번호가 잘못되었습니다")
		return data

	def perform_login(self, request):				
		user = authenticate(username=request.data['username'], password=request.data['password'])
		login(request, user)
		return user



class TransactionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Transaction
		fields = ['id', 'account', 'type', 'coin', 'price', 'total_price', 'coin_amount']

	def validate(self, data):
		if data['type'] == 'buy' and data['account'].balance < data['total_price']:
			raise serializers.ValidationError('보유 금액이 부족합니다')
		
		return data

	def create(self, validated_data):
		transaction = Transaction.objects.create(**validated_data)

		return transaction


class AccountSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=True)
	balance = serializers.IntegerField(read_only=True)
	transactions = TransactionSerializer(many=True, read_only=True)
	coinholdings = CoinHoldingSerializer(many=True, read_only=True)

	class Meta:
		model = Account
		fields = ['user', 'balance', 'transactions', 'coinholdings']

	def validate(self, data):
		user_data = data['user']
		UserSerializer(data=user_data).is_valid(raise_exception=True)
		return data

	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = UserSerializer.create(UserSerializer(), validated_data=user_data)
		account = Account.objects.create(user=user)

		return account

	def update(self, instance, validated_data):
		user = instance.user
		user_data = validated_data.pop('user')
		user = UserSerializer.update(UserSerializer(), instance=user, validated_data=user_data)
		instance.save()

		return instance