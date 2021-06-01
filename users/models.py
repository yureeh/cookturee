from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    propic = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return {self.user.username}

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.propic.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.propic.path)