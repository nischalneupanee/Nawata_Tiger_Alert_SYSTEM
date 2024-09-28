import time

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class CustomUser(AbstractUser):
    username = None
    Name = models.CharField(max_length=150)
    Contact_no = models.CharField(max_length=100, unique=True)

    email=models.EmailField(max_length=100,default="Not required")

    USERNAME_FIELD = 'Contact_no'

    Reason_for_membership=models.CharField(max_length=1000,null=True)

    occupation=models.CharField(max_length=1000,null=True)

    identity=models.ImageField(upload_to='identity_images/',default="images/profile.jpg")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    verified=models.BooleanField(default=False)


    objects=UserManager()




