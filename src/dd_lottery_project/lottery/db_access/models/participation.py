from django.db import models
from django.utils import timezone

from .base_model import BaseModel


from enum import Enum

class ParticipationState(Enum):
    CONFIRMED_PARTICIPATION =        (1, 'Participating')
    WINNER =                         (2, 'Winner')

REGISTRATION_PENDING = (0, 'Registration pending')

PARTICIPATION_STATES = tuple([REGISTRATION_PENDING] + [(x.value[0], x.value[1]) for x in list(ParticipationState)])


class Participation(models.Model):

    code = models.TextField(primary_key=True, verbose_name="This is the unique token a participant has to use, to signify he participates", help_text="Should be a 'difficult' string to guess")
    state = models.IntegerField(choices=PARTICIPATION_STATES, default=REGISTRATION_PENDING)

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.code:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)