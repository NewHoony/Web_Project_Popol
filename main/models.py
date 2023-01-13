from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pic = models.ImageField(upload_to="user/%y/%m")
    comment = models.TextField()

    def getpic(self):
        if self.pic:
            return self.pic.url
        return "/media/noimage.png"

# Create your models here.
