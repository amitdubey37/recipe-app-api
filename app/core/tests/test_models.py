from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a user with email is successful"""
        email = "amit@mail.com"
        password = "Test@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEquals(user.email, email)
        self.assertEquals(True, user.check_password(password))

    def test_create_new_user_email_is_normalized(self):
        """New users email is normalized """
        emaill = "amit@GmAIL.COM"
        user = get_user_model().objects.create_user(
            email=emaill,
            password='test123'
        )
        self.assertEquals(user.email, emaill.lower())

    def test_new_user_invalid_email(self):
        """Creating a new user without email shoudl fail"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test@123')

    def test_create_superuser(self):
        """Test new super user"""
        user = get_user_model().objects.create_superuser(
            email='test@mail.com',
            password='test@123'
        )
        self.assertEquals(True, user.is_staff)
        self.assertEquals(True, user.is_superuser)
