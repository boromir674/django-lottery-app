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
    #
    #     for p in participations:
    #         _ = ParticipationsTable(p, competition)
    #         _.save()
    #
    # def add_random(self, code_generator):
    #     _ = Participation.objects.random(code_generator)
    #     for a in _:
    #         print(a)
    #     self.participations.add(*_)
    #

class ParticipationsTable(BaseModel):
    objects = ParticipationsTableManager()  # attach custom manager (not a table field/column)

    participation = models.ForeignKey(Participation, models.CASCADE)
    competition = models.ForeignKey(Competition, models.CASCADE)
