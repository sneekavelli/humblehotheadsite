from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.



class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)

def __str__(self):
    return self.user.username
