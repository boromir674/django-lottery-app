from django.db import models
from django.utils import timezone


class Receit(models.Model):

    width = models.FloatField(unique=True, help_text="Physical width in centimeters")

