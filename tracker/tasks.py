from django.db import IntegrityError
from app import app
from .types import CALLER_TYPES
from .models import PersonEvent, PersonData, PersonContact


@app.task()
def handle_background(caller_type, person_id, caller_name, caller_value):
    from .services import get_or_create_person
    caller_type = int(caller_type)
    print("begin handle background!")
    person = get_or_create_person(person_id)
    print([person_id, person.uid)
    if caller_type == CALLER_TYPES['EVENT']:
        print('starting event')
        p = PersonEvent.objects.create(person=person, event_name=caller_name, event_value=caller_value)
        print(p.person.uid)
    elif caller_type == CALLER_TYPES['CONTACT']:
        print('starting contact')
        try:
            p = PersonContact.objects.create(person=person, contact_type=caller_name, contact_value=caller_value)
            print('done ' + p.person.uid)
        except IntegrityError:
            print('fail, print debug')
    elif caller_type == CALLER_TYPES['DATA']:
        print('starting data')
        try:
            p = PersonData.objects.create(person=person, data_type=caller_name, data_value=caller_value)
            print('done ' + p.person.uid)
        except IntegrityError:
            print('fail, print debug')
    else:
        print("some error")
    print('done background, print debug')
