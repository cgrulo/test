# coding: utf8
from django.db import models

from apps.utils import create_id
from apps.users.models import Profile




class LocationModel(models.Model):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            coordinates --  Latitude and Longuitude as string.
                            example. "19.4094937,-99.1634261"
            geometry -- Similar to coordinate but using with postgis
    """

    id = models.CharField(default=' ', primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return self.id


    def get_user_profile(self, request):
        user = request.user
        profiles = Profile.objects.filter(user=user)
        for profile in profiles:
            tipo = profile.tipo
        return tipo

    def save(self, *args, **kwargs):
        exists = LocationModel.objects.filter(id=self.id).exists()
        if not exists:
            self.id = create_id('loc_')
        super(LocationModel, self).save(*args, **kwargs)
