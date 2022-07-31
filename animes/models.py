from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
  ...


class Image(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images/')


# Create your models here.
class Tag(models.Model):
  name = models.TextField(null=False, max_length=50)


class Anime(models.Model):
  name = models.TextField(max_length=255)
  episodes = models.IntegerField(null=False, default=0)
  seasons = models.IntegerField(null=False, default='')
  description = models.TextField()
  images = models.ManyToManyField(Image)
  tags = models.ManyToManyField(Tag)


class Review(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
