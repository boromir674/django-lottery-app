from django.db import models

from .business import Business
from .base_model import BaseModel


class Product(models.Model):

    # REQUIRED
    name = models.TextField()
    description = models.TextField()

    # OPTIONAL
    value = models.TextField(default=0.1, null=True, blank=True)
    image = models.URLField(null=True, blank=True)

    # FOREIGN KEY
    business = models.ForeignKey(Business, models.CASCADE)

    def __str__(self):
        return self.name
