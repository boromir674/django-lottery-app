from django.db import models

from .base_model import BaseModel


class Receit(BaseModel):

    width = models.FloatField(primary_key=True, name="Physical width in centimeters")
