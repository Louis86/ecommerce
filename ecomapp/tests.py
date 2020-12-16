from django.test import TestCase
from django.core import urlresolvers
import httplib
# Create your tests here.

from .models import Category, Product



class Authentification(TestCase):
    def setUp(self):
        User(username="test@test.com", password="test")
