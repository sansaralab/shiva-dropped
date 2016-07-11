import uuid
from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField
from .types import TRIGGER_ACTION_TYPE_CHOICES


class Person(models.Model):
    uid = models.UUIDField(unique=True, null=False, blank=False, default=uuid.uuid1, editable=False)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Person, self).save(*args, **kwargs)


class PersonVisit(models.Model):
    person = models.ForeignKey(Person)
    page = models.TextField(blank=True, null=False)
    user_agent = models.TextField(blank=True, null=False)
    user_ip = models.GenericIPAddressField(blank=True, null=True)
    created_at = models.DateTimeField(editable=False, default=timezone.now)


class PersonContact(models.Model):
    """
    Only for storing person's contacts
    """
    person = models.ForeignKey(Person)
    contact_type = models.TextField(blank=False, null=False, db_index=True)
    contact_value = models.TextField(blank=False, null=False, db_index=True)
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        unique_together = (("person", "contact_type", "contact_value"),)


class PersonData(models.Model):
    """
    For storing any additional information about person
    """
    person = models.ForeignKey(Person)
    data_type = models.TextField(blank=False, null=False, db_index=True)
    data_value = models.TextField(blank=False, null=False, db_index=True)
    created_at = models.DateTimeField(editable=False, default=timezone.now)

    class Meta:
        # TODO: is unique necessary?
        unique_together = (("person", "data_type", "data_value"),)


class PersonEvent(models.Model):
    person = models.ForeignKey(Person)
    event_name = models.TextField(blank=False, null=False)
    event_value = models.TextField(blank=True, null=False, default='')
    created_at = models.DateTimeField(editable=False, default=timezone.now)


class Trigger(models.Model):
    """
    This is core entity of entire application
    """
    name = models.TextField(blank=False, null=False)
    active = models.BooleanField(blank=False, null=False, default=True)
    action_type = models.IntegerField(null=False, choices=TRIGGER_ACTION_TYPE_CHOICES)
    conditions = JSONField(null=True)
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.modified_at = timezone.now()
        return super(Trigger, self).save(*args, **kwargs)
