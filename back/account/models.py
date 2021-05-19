from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	balance = models.PositiveBigIntegerField(default=0)

# Create your models here.
