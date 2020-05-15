from enum import Enum
from django.db import models
from django.utils import timezone


REGISTRATION_PENDING = (0, 'Registration pending')

class ParticipationState(Enum):
    CONFIRMED_PARTICIPATION =        (1, 'Participating')
    WINNER =                         (2, 'Winner')


PARTICIPATION_STATES = tuple([REGISTRATION_PENDING] + [(x.value[0], x.value[1]) for x in list(ParticipationState)])


# cc = CodeGenerator.from_django_settings(6, 7, codes=[p.code for p in iter(Pa)])
# code_generator = from_lottery_db(cls, code_length, nb_codes, participation_model, **kwargs)

class ParticipationManager(models.Manager):
    # code_generator = CodeGenerator.from_django_settings(6, 20)
    # code_generator = cg

    def _participation(self, code):
        _ = Participation(code=code, state=0)
        _.save()
        return _

    def random(self, code_generator, **kwargs):
        # self.code_generator = CodeGenerator.from_django_settings(number, length, codes=[p.code for p in iter(self)])
        number = int(kwargs.get('number', 0))
        code_length = int(kwargs.get('length', 0))
        self.code_generator.nb_codes = number
        self.code_generator.code_length = code_length
        return [self._participation(code) for code in iter(code_generator)]


class Participation(models.Model):
    objects = ParticipationManager()

    code = models.TextField(primary_key=True, verbose_name="This is the unique token a participant has to use, to signify he participates", help_text="Should be a 'difficult' string to guess")
    state = models.IntegerField(choices=PARTICIPATION_STATES, default=REGISTRATION_PENDING)

    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(editable=False, null=True)

    def save(self, *args, **kwargs):
        if not self.code:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)

