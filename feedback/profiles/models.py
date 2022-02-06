from pyexpat import model
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    image = models.ImageField(upload_to=("images")) # w.r.t MEDIA_ROOT @settings.py
