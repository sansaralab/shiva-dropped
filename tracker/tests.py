import uuid
from django.test import TestCase
from .services import create_new_site_visitor
from .models import Person, PersonVisit


class PersonManageTestCase(TestCase):
    def test_create_new_person(self):
        old_count = Person.objects.count()
        create_new_site_visitor()
        new_count = Person.objects.count()
        self.assertEquals(old_count + 1, new_count)

    def test_person_uuid(self):
        person = create_new_site_visitor()
        has_error = False
        try:
            uuid.UUID(str(person.uid), version=1)
        except Exception:
            has_error = True
        self.assertFalse(has_error)

    def test_serving_shiva_js(self):
        resp = self.client.get('/tracker/shiva.js')
        self.assertEquals(resp.status_code, 200)

    def test_client_visit_log(self):
        old_visits = PersonVisit.objects.count()
        succ_resp = self.client.get('/tracker/track', {'p': 'test_page'})
        self.assertEquals(succ_resp.status_code, 200)
        new_total_visits = PersonVisit.objects.count()
        self.assertEquals(old_visits + 1, new_total_visits)

    def test_client_visit_fail_log(self):
        fail_resp = self.client.get('/tracker/track')
        self.assertEquals(fail_resp.status_code, 403)

    def test_additional_information(self):
        resp = self.client.get('/tracker/attach', {'t': 'email', 'v': 'testmail@example.com'})
        self.assertEquals(resp.status_code, 200)
        uid = self.client.cookies.get('uid').value
        count = Person.objects.filter(uid=uid, personinfo__info_type='email',
                                      personinfo__info_value='testmail@example.com').count()
        self.assertEquals(count, 1)
