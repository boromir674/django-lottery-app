from django.db import models
from django.utils import timezone


class BaseModel(models.Model):

    class Meta:  # give a model metadata (ie enything that is not a field)
        abstract = True  # If abstract = True, this model will be an abstract base class.

    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super().save(*args, **kwargs)
