import uuid
from django.db import models
from .types import TRIGGER_ACTION_TYPE_CHOICES


class Person(models.Model):
    uid = models.UUIDField(unique=True, null=False, blank=False, default=uuid.uuid1, editable=False)


class PersonVisit(models.Model):
    person = models.ForeignKey(Person)
    page = models.TextField(blank=True, null=False)
    user_agent = models.TextField(blank=True, null=False)
    user_ip = models.GenericIPAddressField(blank=True, null=True)
    visit_time = models.DateTimeField(auto_now=True, null=False)


class PersonInfo(models.Model):
    person = models.ForeignKey(Person)
    info_type = models.TextField(blank=False, null=False, db_index=True)
    info_value = models.TextField(blank=False, null=False, db_index=True)

    class Meta:
        unique_together = (("person", "info_type", "info_value"),)


class PersonEvent(models.Model):
    person = models.ForeignKey(Person)
    event_name = models.TextField(blank=False, null=False)
    event_value = models.TextField(blank=True, null=False, default='')


class Trigger(models.Model):
    """
    This is core entity of entire application
    """
    name = models.TextField(blank=False, null=False)
    action_type = models.IntegerField(null=False, choices=TRIGGER_ACTION_TYPE_CHOICES)
