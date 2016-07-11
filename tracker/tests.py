import uuid
from django.test import TestCase
from .services import create_new_site_visitor, _get_or_create_person
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

    def test_person_contact(self):
        resp = self.client.get('/tracker/attach', {'t': 'email', 'v': 'testmail@example.com'})
        self.assertEquals(resp.status_code, 200)
        uid = self.client.cookies.get('uid').value
        count = Person.objects.filter(uid=uid,
                                      personcontact__contact_type='email',
                                      personcontact__contact_value='testmail@example.com').count()
        self.assertEquals(count, 1)

    def test_fail_person_contact(self):
        resp = self.client.get('/tracker/attach')
        self.assertEquals(resp.status_code, 403)

    def test_duplicate_person_contact(self):
        resp = self.client.get('/tracker/attach', {'t': 'email', 'v': 'duplicate@example.com'})
        self.assertEquals(resp.status_code, 200)
        resp = self.client.get('/tracker/attach', {'t': 'email', 'v': 'duplicate@example.com'})
        self.assertEquals(resp.status_code, 200)

    def test_person_data(self):
        resp = self.client.get('/tracker/data', {'t': 'birthday', 'v': '1900-01-01'})
        self.assertEquals(resp.status_code, 200)
        uid = self.client.cookies.get('uid').value
        count = Person.objects.filter(uid=uid,
                                      persondata__data_type='birthday',
                                      persondata__data_value='1900-01-01').count()
        self.assertEquals(count, 1)

    def test_fail_person_data(self):
        resp = self.client.get('/tracker/data')
        self.assertEquals(resp.status_code, 403)

    def test_duplicate_person_data(self):
        resp = self.client.get('/tracker/data', {'t': 'duplicate', 'v': 'duplicate'})
        self.assertEquals(resp.status_code, 200)
        resp = self.client.get('/tracker/data', {'t': 'duplicate', 'v': 'duplicate'})
        self.assertEquals(resp.status_code, 200)

    def test_send_person_event(self):
        uniq_val = str(uuid.uuid4())
        resp = self.client.get('/tracker/event', {'t': 'test_name', 'v': uniq_val})
        self.assertEquals(resp.status_code, 200)
        uid = self.client.cookies.get('uid').value
        count = Person.objects.filter(uid=uid,
                                      personevent__event_name='test_name',
                                      personevent__event_value=uniq_val).count()
        self.assertEquals(count, 1)

    def test_fail_send_person_event(self):
        resp = self.client.get('/tracker/event')
        self.assertEquals(resp.status_code, 403)

    def test_person_creation(self):
        first = _get_or_create_person('invalid uid')
        second = _get_or_create_person('invalid uid')
        self.assertFalse(str(first.uid) == str(second.uid))
        third = _get_or_create_person('c2b5ecab-47a1-11e6-af5a-080027b379fa')
        fourth = _get_or_create_person('c2b5ecab-47a1-11e6-af5a-080027b379fa')
        self.assertEquals(str(third.uid), str(fourth.uid))
