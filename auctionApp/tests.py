from django.test import TestCase
from django.contrib import auth

from auctionApp.models import CustomUser

TEST_USERNAME = 'user33'
TEST_PASSWORD = 'user33'


class UserTestCase(TestCase):

    def setUp(self):
        config = User.objects.create(username=TEST_USERNAME)
        config.set_password(TEST_PASSWORD)
        # need to save after setting password
        config.save()