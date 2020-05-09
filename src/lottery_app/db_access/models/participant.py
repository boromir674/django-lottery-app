from django.db.models import fields as f
from django.db.models import

from .base_model import BaseModel


class Participant(BaseModel):

    code = f.TextField(help_text="Should be a 'difficult' string to guess")
    competition = f.C