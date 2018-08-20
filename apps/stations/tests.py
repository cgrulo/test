# coding: utf8
from django.urls import reverse

from rest_framework.test import APITestCase

from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import LocationFactory, StationFactory
from apps.stations.models import LocationModel, StationModel


class LocationCreateTest(APITestCase):

    url = reverse("api:v1_list_create_location")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        LocationFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_create_successfully(self):
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, 201)


#---------------Aun no sirve-------------------------

# class LocationUpdateTest(APITestCase):
#
#     def setUp(self):
#         self.user = UserFactory()
#         self.user_token = TokenFactory(user=self.user)
#
#         self.client.credentials(
#             HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
#         )
#     def test_update_successfully(self):
#
#         data = {
#             "name": "Urbvan",
#             "latitude": 19.388401,
#             "longitude": -99.227358
#         }
#
#         location = LocationModel(name=data['name'], latitude=data['latitude'], longitude=data['longitude'])
#         location.save()
#
#         self.url = reverse("api:v1_update_location", kwargs={'id': location.id})
#         #self.url = '/v1/api/locations/update/'+ location.id + '/'
#         data_mod = {
#             "id": location.id,
#             "name": "UrbvanUpdated",
#             "latitude": 19.388401,
#             "longitude": -99.227358
#         }
#
#         response = self.client.post(self.url, data_mod, format='json')
#         self.assertEqual(response.status_code, 200)


class StationCreateTest(APITestCase):

    url = reverse("api:v1_list_station")

    def setUp(self):
        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_list(self):
        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        location = LocationModel(name=data['name'], latitude=data['latitude'], longitude=data['longitude'])
        location.save()
        StationFactory(location)

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    # def test_create_successfully(self):
    #     data = {
    #         "name": "Urbvan",
    #         "latitude": 19.388401,
    #         "longitude": -99.227358
    #     }
    #     location = LocationModel(name=data['name'], latitude=data['latitude'], longitude=data['longitude'])
    #     location.save()
    #
    #     data2 = {
    #         'location': location,
    #         'order': 5,
    #         'is_active': 'True',
    #     }
    #
    #     response = self.client.post(self.url, data2, format='json')
    #     self.assertEquals(response.status_code, 201)
