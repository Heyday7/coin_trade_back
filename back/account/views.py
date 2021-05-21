from django.contrib.auth import logout
from .serializers import AccountSerializer, LoginSerializer, TransactionSerializer
from django.shortcuts import get_object_or_404
from rest_framework import views, viewsets
from rest_framework.response import Response
from .models import Account
from coin.utils import get_coin_price
from coin.models import Coin, CoinHolding
from coin.serializers import CoinHoldingSerializer


class AccountViewSet(viewsets.ModelViewSet):
	queryset = Account.objects.all()
	serializer_class = AccountSerializer


class LoginView(views.APIView):
	def post(self, request, *args, **kwargs):
		serializer = LoginSerializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		serializer.perform_login(request)
		return Response(serializer.data)


class LogoutView(views.APIView):
	def post(self, request, *args, **kwargs):
		logout(request)
		return Response()


class TransactionView(views.APIView):
    def post(self, request, *args, **kwargs):
        price = get_coin_price(request.data['ticker'])['data']['closing_price']
        coin, create = Coin.objects.get_or_create(ticker=request.data['ticker'])
        data = {**request.data, 
            "price":price, 
            "coin":coin.id,
            "account" : Account.objects.get(user=self.request.user).id,
            "total_price": float(price) * request.data['coin_amount']
        }
        tran_seri = TransactionSerializer(data=data)

        try:
            instance = get_object_or_404(CoinHolding, account=data['account'], coin=data['coin'])
            coin_hold_seri = CoinHoldingSerializer(instance=instance, data=data)
        except:
            coin_hold_seri = CoinHoldingSerializer(data=data)

        tran_seri.is_valid(raise_exception=True)
        coin_hold_seri.is_valid(raise_exception=True)
        tran_seri.save()
        coin_hold_seri.save()

        return Response(tran_seri.data)