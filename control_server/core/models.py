from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=50)
    address = models.GenericIPAddressField(unique=True)
    user = models.ForeignKey(User, related_name='cars')

    def __str__(self):
        return self.name

