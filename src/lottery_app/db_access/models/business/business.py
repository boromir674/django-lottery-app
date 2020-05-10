from django.db import models as md

from src.lottery_app.db_access.models.base_model import BaseModel


class Business(BaseModel):

    name = md.TextField(max_length=20)  # keep short to render in front-end
    description = md.TextField()
    email = md.EmailField()
    address = md.TextField()
    receit_specs = md.ForeignKey()