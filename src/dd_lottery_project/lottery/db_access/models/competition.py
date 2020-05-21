from django.db import models

from .base_model import BaseModel
from .participation import Participation

from lottery.utils import CodeGenerator


class CompetitionManager(models.Manager):

    def find_competition(self, code):
        for comp in iter(self):
            if comp.is_belonging(code):
                return comp
        return None


class Competition(BaseModel):
    """A competition involves a prize pool, contestants and drawings"""
    # Schema
    name = models.TextField()
    begin_date = models.DateField()
    end_date = models.DateField()
    is_running = models.BooleanField()
    participations = models.ManyToManyField(Participation, through='ParticipationsTable')
    # code_length = models.PositiveSmallIntegerField(default=6, name='code length', verbose_name='Length of the codes that participate in this competition.', )

    objects = CompetitionManager()

    def is_belonging(self, code):
        """Call this method to simply check if code has been generated as part of this competition."""
        for participation in self.participations:
            if code == participation.code:  # query happens here
                return True
        return False

    def is_winning(self, code):
        """Call this method to check if a code is winning."""
        for participation in self.participations:
            if code == participation.code:  # query happens here
                return participation.state == 3
        raise MissingCodeError("The requested '%d' code does not belong in this competition.", code)

    def is_participating(self, code):
        """Call this method to check if the code is flagged as confirmed to participate in the (upcoming) lottery."""
        for participation in self.participations:
            if code == participation.code:  # query happens here
                return participation.state == 3
        raise MissingCodeError("The requested '%d' code does not belong in this competition.", code)


class MissingCodeError(Exception): pass
