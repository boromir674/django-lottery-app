from django.db import models
from django.utils import timezone


class Receit(models.Model):

    width = models.FloatField(name="Physical width in centimeters")

    # created = models.DateTimeField(editable=False)
    # modified = models.DateTimeField(editable=False)
    #
    # def save(self, *args, **kwargs):
    #     if not self.width:
    #         self.created = timezone.now()
    #     self.modified = timezone.now()
    #     return super().save(*args, **kwargs)
