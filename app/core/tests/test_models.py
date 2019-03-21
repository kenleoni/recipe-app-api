from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user():
    """Create a sample user"""
    return get_user_model().objects.create_user(
        email='test@kandlem.com',
        password='testpass',
    )


class ModelTests(TestCase):
    """docstring for ModelTests."""

    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful"""
        email = "test@kandlem.com"
        password = "TestPass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test if the email for a new email is normalised"""
        email = "test@KANDLEM.COM"
        user = get_user_model().objects.create_user(email, 'test1234')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test1234')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@kandlem.com',
            'test1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )

        self.assertEqual(str(tag), tag.name)
