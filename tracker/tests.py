from django.test import TestCase
from .services import create_new_site_visitor
from .models import Person, PersonInfo, PersonVisit


class PersonManageTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_new_person(self):
        uid = create_new_site_visitor().uid
        count = Person.objects.filter(uid=uid).count()
        self.assertEquals(count, 1)
