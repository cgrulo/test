# coding: utf8
from django.db import models

from .locations import LocationModel

from apps.utils import create_id


class StationModel(models.Model):

    id = models.CharField(default=' ', primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(LocationModel, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.id

    #solo si no existe genera el id
    def save(self, *args, **kwargs):
        exists = StationModel.objects.filter(id=self.id).exists()
        if not exists:
            self.id = create_id('loc_')
        super(StationModel, self).save(*args, **kwargs)