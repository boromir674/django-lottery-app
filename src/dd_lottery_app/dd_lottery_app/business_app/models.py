from django.db import models

# Create your models here.

from src.lottery_app.db_access.models.base_model import BaseModel


class Receit(BaseModel):
    width = models.FloatField(primary_key=True, name="Physical width in centimeters")


class Business(BaseModel):

    name = models.TextField(max_length=20)  # keep short to render in front-end
    description = models.TextField()
    email = models.EmailField()
    address = models.TextField()
    receit_specs = models.ForeignKey(Receit, models.CASCADE)
