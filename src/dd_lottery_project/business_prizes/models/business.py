from django.conf import settings
from django.db import models

from .receit import Receit
from .base_model import BaseModel


class BusinessManager(models.Manager):
    def nb_businesses_with_receit(self):
        return self.filter(receit__isnull=True).count()


class Business(BaseModel):
    objects = BusinessManager()

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    description = models.TextField()
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)

    receit = models.ForeignKey(Receit, models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name