from django.test import TestCase
from core.models import Company


class TestCore(TestCase):
    def setUp(self):
        Company.objects.create(name="Test Company")

    def test_company_create(self):
        company = Company.objects.get(name="Test Company")
        self.assertEqual(str(company), "Test Company")

