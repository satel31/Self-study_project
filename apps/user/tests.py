from rest_framework import status
from rest_framework.test import APITestCase

from apps.user.models import User


class UserTestCase(APITestCase):

    def setUp(self) -> None:
        self.url = '/users/'
        self.user = User.objects.create(email='test@example.com', password='test')
        self.client.force_authenticate(user=self.user)

    def test_1_create_user(self):
        """User creation testing """
        data = {
            'email': 'test2@example.com',
            'password': 'test'
        }
        response = self.client.post(f'{self.url}add_user/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(User.objects.all().count(), 2)

    def test_2_list_user(self):
        """User list testing """
        response = self.client.get(f'{self.url}users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'first_name': None, 'email': 'test@example.com', 'city': None, 'avatar': None, 'phone': None,
              'telegram': ''}]
        )

    def test_3_retrieve_user(self):
        """User retrieve testing """

        response = self.client.get(f'{self.url}users/{self.user.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'first_name': None, 'last_name': None, 'email': 'test@example.com', 'city': None, 'avatar': None,
             'phone': None, 'password': 'test'}

        )

    def test_4_update_user(self):
        """User update testing """
        data = {
            'email': 'test2@example.com',
            'password': 'test'
        }

        response = self.client.put(f'{self.url}users/update/{self.user.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'first_name': None, 'last_name': None, 'email': 'test2@example.com', 'city': None, 'avatar': None,
             'phone': None, 'password': response.json()['password']}
        )

    def test_5_update_partial_user(self):
        """User partial update testing """
        data = {
            'email': 'test2@example.com'
        }
        response = self.client.patch(f'{self.url}users/update/{self.user.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(
            response.json(),
            {'first_name': None, 'last_name': None, 'email': 'test2@example.com', 'city': None, 'avatar': None,
             'phone': None, 'password': response.json()['password']}
        )

    def test_6_destroy_user(self):
        """User destroying testing """
        response = self.client.delete(f'{self.url}users/delete/{self.user.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertFalse(User.objects.all().exists())

    def test_7_retrieve_stranger_user(self):
        """Stranger User retrieve testing """
        self.stranger_user = User.objects.create(email='test2@example.com', password='test')

        response = self.client.get(f'{self.url}users/{self.stranger_user.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'first_name': None, 'email': 'test2@example.com', 'city': None, 'avatar': None, 'phone': None,
             'telegram': ''}

        )
