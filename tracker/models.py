import uuid
from django.db import models


class Person(models.Model):
    uid = models.UUIDField(unique=True, null=False, blank=False, default=uuid.uuid1, editable=False)


class PersonVisit(models.Model):
    person = models.ForeignKey(Person)
    page = models.TextField(blank=True, null=False)
    user_agent = models.TextField(blank=True, null=False)
    user_ip = models.GenericIPAddressField(blank=True, null=True)
    visit_time = models.DateTimeField(auto_now=True, null=False)
