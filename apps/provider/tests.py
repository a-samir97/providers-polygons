from django.test import TestCase
from rest_framework import status
from model_bakery import baker
from . import models


class TestProviderAPIs(TestCase):

    def setUp(self):
        self.provider = baker.make(
            models.Provider,
            phone_number='+201112221122')
        self.provider_url = '/api/providers/'
        self.provider_details_url = '/api/providers/{id}/'

    def tearDown(self):
        models.Provider.objects.all().delete()

    def test_create_provider_success_case(self):
        data = {
            'name': 'test_name',
            'email': 'test@gmail.com',
            'phone_number': '+201112221122',
            'language': 'English',
            'currency': 'USD'
        }
        response = self.client.post(self.provider_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_create_provider_failure_case_with_no_data(self):
        response = self.client.post(self.provider_url)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.data)
        self.assertIn('email', response.data)
        self.assertIn('phone_number', response.data)
        self.assertIn('language', response.data)

    def test_create_provider_failure_case_with_invalid_data(self):
        data = {
            'name': 'test_name',
            'email': 'test',  # invalid email
            'phone_number': '+201112221122',
            'language': 'English',
            'currency': 'USD'
        }

        response = self.client.post(self.provider_url, data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', response.data)

    def test_get_provider_success_case(self):
        response = self.client.get(
            self.provider_details_url.format(
                id=self.provider.id))
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(response.data['name'], self.provider.name)
        self.assertEquals(response.data['email'], self.provider.email)
        self.assertEquals(
            response.data['phone_number'],
            self.provider.phone_number)
        self.assertEquals(response.data['language'], self.provider.language)

    def test_get_provider_failure_case_not_found(self):
        response = self.client.get(
            self.provider_details_url.format(
                id=10000000))  # not exist
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_list_providers_success_case(self):
        response = self.client.get(self.provider_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_update_provider_success_case(self):
        pass

    def test_update_provider_failure_case_not_found(self):
        response = self.client.put(
            self.provider_details_url.format(
                id=100000))  # not exit
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_provider_failure_case_not_valid_data(self):
        data = {
            'name': 'test_name',
            'email': 'test',  # invalid email
            'phone_number': '+201112221122',
            'language': 'English',
            'currency': 'USD'
        }
        response = self.client.put(
            self.provider_details_url.format(
                id=self.provider.id),
            data,
            content_type='application/json')
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_provider_success_case(self):
        response = self.client.delete(
            self.provider_details_url.format(
                id=self.provider.id))
        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_provider_failure_case_not_found(self):
        response = self.client.delete(
            self.provider_details_url.format(
                id=10000000))  # not exist
        self.assertEquals(response.status_code, status.HTTP_404_NOT_FOUND)
