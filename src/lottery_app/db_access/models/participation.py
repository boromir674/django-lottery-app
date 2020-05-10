from django.db import models

from .base_model import BaseModel
from .competition import Competition


class Participation(BaseModel):

    code = models.TextField(verbose_name="This is the unique token a participant has to use to authenticate", help_text="Should be a 'difficult' string to guess")
    competition = models.ForeignKey(Competition, models.CASCADE)
    registered = models.BooleanField(verbose_name="Indicates whether a participant registered his/her ticket.", default=False)

