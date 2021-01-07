from django.test import TestCase
# Create your tests here.
#e l’accès à une base de données pour créer ou interroger des modèles
from .models import Category, Product
#
#coverage report


class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(title="jouet", slug="jouet")
        Category.objects.create(title="multimedia", slug="multimedia")

    def test_category(self):
        jouet = Category.objects.get(title="jouet")
        multimedia = Category.objects.get(title="multimedia")
        self.assertEqual(str(jouet), "jouet")
        self.assertEqual(str(multimedia), "multimedia")



class ProductTestCase(TestCase):
    def setUp(self):
        self.cat = Category.objects.create(title="category1", slug="category1")
        Product.objects.create(category = self.cat, title="product1", slug="slug_product1", description="descriptions_product1",price = 12 )

    def test_Product(self):
        dp1 = Product.objects.get(description="descriptions_product1")
        self.assertEqual(str(dp1), "product1")

    def test_view_url_exists(self):
        response = self.client.get('/ecomapp/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_product(self):
        response2 = self.client.get('/ecomapp/products/')
        self.assertEqual(response2.status_code, 200)
