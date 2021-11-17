import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    full_name   = models.CharField(max_length=40,unique=True)
    email       = models.EmailField(unique=True)
    password    = models.CharField(max_length=400)
    secrete_key = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
    	return '{}'.format(str(self.full_name))