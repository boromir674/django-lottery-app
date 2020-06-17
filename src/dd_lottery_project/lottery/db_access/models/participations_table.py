from django.db import models

from .participation import Participation
from .competition import Competition
from .base_model import BaseModel

from lottery.utils import CodeGenerator


class ParticipationsTableManager(models.Manager):

    def new_random(self, competition, code_generator):
        partcipations = Participation.objects.random(code_generator)
        for part in partcipations:
            part.save()
            _ = ParticipationsTable(participation=part, competition=competition)
            _.save()

class ParticipationsTable(BaseModel):
    objects = ParticipationsTableManager()  # attach custom manager (not a table field/column)

    participation = models.ForeignKey(Participation, models.CASCADE)
    competition = models.ForeignKey(Competition, models.CASCADE)
