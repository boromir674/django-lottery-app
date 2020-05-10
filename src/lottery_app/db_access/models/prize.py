from django.db.models import fields as f

from .base_model import BaseModel


class Prize(BaseModel):

    name = f.TextField(max_length=20)
    description = f.TextField()
    value = f.FloatField()


# address
# phone
# name
# list of products

{
    "name": "a name",
    "address": "",
    "descriptiob": "",
    "items": [
        {"value": 10,
         "name": "AA",
         "descr": "optional",
         "count": 2},
        {"value": 98,
         "name": "BB",
         "descr": "optional",
         "count": 1}
    ]
}