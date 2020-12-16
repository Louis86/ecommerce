from django.db import models
import uuid
# Create your models here.
class Profile(models.Model):
    user_id = models.IntegerField()
    role = models.IntegerField() # 0: shopper, 1: seller
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    zip = models.CharField(max_length=10)
