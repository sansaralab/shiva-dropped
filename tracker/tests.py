from django.test import TestCase
from .services import create_new_site_visitor
from .models import Person, PersonVisit


class PersonManageTestCase(TestCase):
    def setUp(self):
        pass

    def test_create_new_person(self):
        uid = create_new_site_visitor().uid
        count = Person.objects.filter(uid=uid).count()
        self.assertEquals(count, 1)

    def test_serving_shiva_js(self):
        resp = self.client.get('/tracker/shiva.js')
        self.assertEquals(resp.status_code, 200)

    def test_client_visit_log(self):
        old_visits = PersonVisit.objects.count()
        succ_resp = self.client.get('/tracker/track', {'p': 'test_page'})
        self.assertEquals(succ_resp.status_code, 200)
        new_total_visits = PersonVisit.objects.count()
        self.assertEquals(old_visits+1, new_total_visits)

    def test_client_visit_fail_log(self):
        fail_resp = self.client.get('/tracker/track')
        self.assertEquals(fail_resp.status_code, 403)
