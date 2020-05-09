from django.db.models import fields as f

from .base_model import BaseModel


class Business(BaseModel):

    name = f.TextField(max_length=20)  # keep short to render in front-end
    description = f.TextField()
    email = f.EmailField()
