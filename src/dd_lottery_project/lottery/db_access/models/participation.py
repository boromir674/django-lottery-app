from django.db import models

from .base_model import BaseModel


from enum import Enum

class ParticipationState(Enum):
    CONFIRMED_PARTICIPATION =        (1, 'Participating')
    WINNER =                         (2, 'Winner')

REGISTRATION_PENDING = (0, 'Registration pending')

PARTICIPATION_STATES = tuple([REGISTRATION_PENDING] + [(x.value[0], x.value[1]) for x in list(ParticipationState)])


class Participation(BaseModel):

    code = models.TextField(verbose_name="This is the unique token a participant has to use, to signify he participates", help_text="Should be a 'difficult' string to guess")
    # competition = models.ForeignKey(Competition, models.CASCADE)
    state = models.IntegerField(choices=PARTICIPATION_STATES, default=REGISTRATION_PENDING)
