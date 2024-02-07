from django.test import TestCase
from django.contrib.auth import get_user_model
from User.models import User, UserRegions

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing
        cls.user = get_user_model().objects.create_user(
            email='test@example.com',
            password='testpassword@123',
            first_name='John',
            last_name='Doe',
            phone='1234567890',
            all_regions=False,
            is_deleted=False
        )

    def test_user_creation(self):
        user = User.objects.get(email='test@example.com')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.phone, '1234567890')
        self.assertEqual(user.all_regions, False)
        self.assertEqual(user.is_deleted, False)

    def test_user_regions_creation(self):
        user = User.objects.get(email='test@example.com')
        user_regions = UserRegions.objects.create(user=user)
        self.assertIsInstance(user_regions, UserRegions)
