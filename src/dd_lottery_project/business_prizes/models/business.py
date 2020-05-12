from django.db import models

from .receit import Receit
from .base_model import BaseModel


class Business(BaseModel):

    name = models.TextField(max_length=20)  # keep short to render in front-end
    description = models.TextField()
    email = models.EmailField()
    address = models.TextField()

    receit_specs = models.ForeignKey(Receit, models.CASCADE)
