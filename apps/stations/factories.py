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

#Al tener un campo con foreign key se debe crear el objeto al que se va a asociar,
# en este caso se crea en el test y se inicializa la apuntando al nuevo objeto creado

class StationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = StationModel

    def __init__(self, location):

        self.location = location

    order = int(random.random()*10+1)
    is_active = True




