from django.db.models import fields as f

from .base_model import BaseModel


class Prize(BaseModel):

    name = f.TextField(max_length=20)
    description = f.TextField()
    value = f.FloatField()

