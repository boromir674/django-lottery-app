from django.db import models

from .base_model import BaseModel
from .participation import Participation

from lottery.utils import CodeGenerator


class CompetitionManager(models.Manager):
    code_generator = CodeGenerator.from_django_settings(6, 20, seen_codes=None)

    def find_competition(self, code):
        for comp in iter(self):
            if comp.is_belonging(code):
                return comp
        return None

    def _participation(self, code):
        _ = Participation(code=code, state=0)
        _.save()
        return _

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


class Competition(BaseModel):
    """A competition involves a prize pool, contestants and drawings"""

    name = models.TextField()
    begin_date = models.DateField()
    end_date = models.DateField()
    is_running = models.BooleanField()
    participations  = models.ManyToManyField(Participation, through='ParticipationsTable')

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
