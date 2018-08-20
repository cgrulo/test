# coding: utf8
import factory

from .models import LocationModel, StationModel
import random


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = LocationModel

    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')


class StationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = StationModel

    def __init__(self, location):

        self.location = location

    order = int(random.random()*10+1)
    is_active = True




