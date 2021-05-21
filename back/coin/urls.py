from django.urls import path, include
from rest_framework import urlpatterns
from .views import *

urlpatterns = [
    path('coin', CoinPriceView.as_view(), name='coin'),
]
