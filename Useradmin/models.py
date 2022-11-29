from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class DefaultUser(AbstractUser):
    image = models.FileField(upload_to="profile_images/")
