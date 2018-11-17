from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    run = models.CharField(max_length=20)
    is_cliente = models.BooleanField(default = False)
    is_admin = models.BooleanField(default = False)

    def __str__(self):
        return self.email