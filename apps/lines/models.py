# coding: utf8
from django.db import models

from apps.stations.models import StationModel

from apps.utils import create_id

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class LineModel(models.Model):

    id = models.CharField(default=' ', primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        exists = LineModel.objects.filter(id=self.id).exists()
        if not exists:
            self.id = create_id('line_')
        super(LineModel, self).save(*args, **kwargs)

class RouteModel(models.Model):

    id = models.CharField(default=' ', primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(LineModel, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(StationModel)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        exists = RouteModel.objects.filter(id=self.id).exists()
        if not exists:
            self.id = create_id('route_')
        super(RouteModel, self).save(*args, **kwargs)


# Crear un token automaticamente cuando se guarde un usuario y asociarlo.
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


