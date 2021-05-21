from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Coin, CoinPrice
from .serializers import CoinPriceSerializer

class CoinPriceView(generics.ListAPIView):
    queryset = CoinPrice.objects.all().order_by('-date')
    serializer_class = CoinPriceSerializer

