from django.test import TestCase
# Create your tests here.
#e l’accès à une base de données pour créer ou interroger des modèles
from .models import Category, Product



class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(title="jouet", slug="jouet")
        Category.objects.create(title="multimedia", slug="multimedia")

    def test_category_have_slug(self):
        jouet = Category.objects.get(title="jouet")
        multimedia = Category.objects.get(title="multimedia")
        self.assertEqual(str(jouet), "jouet")
        self.assertEqual(str(multimedia), "multimedia")
