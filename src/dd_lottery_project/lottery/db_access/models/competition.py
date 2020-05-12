from django.db import models

from .base_model import BaseModel
from .participation import Participation


class Competition(BaseModel):
    """A competition involves a prize pool, contestants and drawings"""

    name = models.TextField()
    begin_date = models.DateField()
    end_date = models.DateField()
    is_running = models.BooleanField()
    participations = models.ManyToManyField(Participation, through='ParticipationsTable')
