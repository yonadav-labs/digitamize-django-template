from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='product')
    description = models.TextField()
    price = models.FloatField()
    quantity = models.FloatField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.title
