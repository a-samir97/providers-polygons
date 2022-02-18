from django.test import TestCase
from django.contrib.gis.geos import Polygon
from rest_framework import status
from model_bakery import baker
from . import models
from apps.provider.models import Provider


class TestPolygonAPIs(TestCase):

    def setUp(self):
        self.provider = baker.make(Provider, phone_number='+201112221122')
        self.polygon = baker.make(
            models.Polygon, 
            provider=self.provider,
            geo_info = Polygon(((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0))))

        self.polygon_url = '/api/polygons/'
        self.polygon_details_url = '/api/polygons/{id}/'
        self.polygons_location_url = '/api/polygons/all/'

    def tearDown(self):
        Provider.objects.all().delete()
        models.Polygon.objects.all().delete()

    def test_create_polygon_success_case(self):
        data = {
            "name": "Name y prince",
            "price": 10.0,
            "geo_info": {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [135.0, 45.0],
                        [140.0, 50.0],
                        [145.0, 55.0],
                        [135.0, 45.0],
                    ]
                ],
            },
            "provider": self.provider.id
        }
        response = self.client.post(
            self.polygon_url, data, content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_polygon_failure_case_not_valid_data(self):
        data = {
            "name": "Name y prince",
            "price": 10.0,
            "geo_info": {
                "type": "Polygon",
            },
            "provider": self.polygon.id
        }
        response = self.client.post(self.polygon_url, data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_polygon_failure_case_no_data(self):
        response = self.client.post(self.polygon_url)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_get_polygon_success_case(self):
        response = self.client.get(
            self.polygon_details_url.format(
                id=self.polygon.id))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_get_polygon_failure_case_not_found(self):
        response = self.client.get(
            self.polygon_details_url.format(
                id=100000))  # not exist
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_list_polygon_success_case(self):
        response = self.client.get(self.polygon_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_update_polygon_success_case(self):
        data = {
            "name": "Name y prince",
            "price": 10.0,
            "geo_info": {
                'type': 'Polygon',
                'coordinates': [
                    [
                        [135.0, 45.0],
                        [140.0, 50.0],
                        [145.0, 55.0],
                        [135.0, 45.0],
                    ]
                ],
            },
            "provider": self.provider.id
        }
        response = self.client.put(
            self.polygon_details_url.format(
                id=self.polygon.id),
            data,
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.polygon.refresh_from_db()
        self.assertEquals(response.data['name'], self.polygon.name)
        self.assertEquals(response.data['price'], self.polygon.price)
        self.assertEquals(response.data['provider'], self.polygon.provider.id)
        # self.assertEquals(response.data['geo_info']['coordinates'], self.polygon.geo_info.coords)

    def test_update_polygon_failure_case_no_data(self):
        response = self.client.put(
            self.polygon_details_url.format(
                id=self.polygon.id),
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_polygon_failure_case_not_valid_data(self):
        data = {
            "name": "Name y prince",
            "price": 10.0,
            "geo_info": {
                'type': 'test'},  # invalid
            "provider": self.provider.id
        }
        response = self.client.put(
            self.polygon_details_url.format(
                id=self.polygon.id),
            data,
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_polygon_success_case(self):
        response = self.client.delete(
            self.polygon_details_url.format(
                id=self.polygon.id))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_polygon_failure_case_not_found(self):
        response = self.client.delete(
            self.polygon_details_url.format(
                id=100000))  # not exist
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)


    def test_all_polygons_by_given_location_success_case(self):
        
        data = {
            'lat': 10,
            'lng': 10
        }
        response = self.client.post(self.polygons_location_url, data, content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertNotEquals(len(response.data), 0)

    def test_all_polygons_by_given_location_failure_case_invalid_data(self):
        data = { # invalid data
            'lat': 'lat',
            'lng': 'lng'
        }
        response = self.client.post(self.polygons_location_url, data, content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)