from django.db import IntegrityError
from app import app
from .types import CALLER_TYPES
from .models import PersonEvent, PersonData, PersonContact


@app.task()
def handle_background(caller_type, person_id, caller_name, caller_value):
    from .services import get_or_create_person
    caller_type = int(caller_type)
    person = get_or_create_person(person_id)
    if caller_type == CALLER_TYPES['EVENT']:
        PersonEvent.objects.create(person=person, event_name=caller_name, event_value=caller_value)
    elif caller_type == CALLER_TYPES['CONTACT']:
        try:
            PersonContact.objects.create(person=person, contact_type=caller_name, contact_value=caller_value)
        except IntegrityError:
            print('fail, print debug')
    elif caller_type == CALLER_TYPES['DATA']:
        try:
            PersonData.objects.create(person=person, data_type=caller_name, data_value=caller_value)
        except IntegrityError:
            print('fail, print debug')
    else:
        print("some error")
