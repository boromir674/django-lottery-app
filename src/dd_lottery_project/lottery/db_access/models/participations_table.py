from django.db import models

from .participation import Participation
from .competition import Competition
from .base_model import BaseModel

from lottery.utils import CodeGenerator


class ParticipationsTableManager(models.Manager):
    code_generator = CodeGenerator.from_django_settings(6, 20, seen_codes=None)

    def new_random(self, name, nb_codes, code_length=6, seen_codes=None):
        self.code_generator.nb_codes = nb_codes
        self.code_generator.code_length = code_length
        if not seen_codes:
            seen_codes = set()
        self.code_generator.seen_codes = seen_codes
        participations = [self._participation(code) for code in iter(self.code_generator)]
        competition = Competition(name=name, begin_date='', end_date='', is_running=True, participations=participations)
        competition.save()
        return competition


class ParticipationsTable(BaseModel):
    objects = ParticipationsTableManager()  # attach custom manager (not a table field/column)

    participation = models.ForeignKey(Participation, models.CASCADE)
    competition = models.ForeignKey(Competition, models.CASCADE)
