from django.contrib.auth import logout
from .serializers import AccountSerializer, LoginSerializer
from django.shortcuts import render
from rest_framework import views, viewsets
from rest_framework.response import Response
from .models import Account


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

