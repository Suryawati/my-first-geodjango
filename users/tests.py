from django.test import TestCase

# Create your tests here.

from .models import CustomUser


class UserTestCase(TestCase):
    def setUp(self):
        CustomUser.objects.create(name="merlyn", username="pakah")
        CustomUser.objects.create(name="prawiro", username="merak")

    def usertalk(self):
        """Animals that can speak are correctly identified"""
        lion = CustomUser.objects.get(name="merlyn")
        cat = CustomUser.objects.get(name="prawiro")
        expected_object_name = f'{lion.name}'
        self.assertEqual(expected_object_name, 'Hai just test')
        #self.assertEqual(cat.address(), "Sampang")