from django.shortcuts import render
from rest_framework import generics, serializers
from .models import Coin
from .serializers import CoinSerializer

class CoinView(generics.ListAPIView):
    queryset = Coin.objects.all().order_by('-date')
    serializer_class = CoinSerializer

