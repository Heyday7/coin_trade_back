from django.urls import path, include
from rest_framework import routers, urlpatterns
from .views import *

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'account', AccountViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('transaction', TransactionView.as_view(), name='transaction'),
]
