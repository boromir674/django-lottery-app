from django.db import models

from .base_model import BaseModel


class Competition(BaseModel):
    """A competition involves a prize pool, contestants and drawings"""

    name = models.TextField()

