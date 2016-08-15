from django.db import IntegrityError
from app import app
from .types import ACTION_TYPES
from .models import PersonEvent, PersonData, PersonContact


@app.task()
def handle_background(caller_type, person_id, caller_name, caller_value):
    from .services import get_or_create_person
    from .handlers import handle_backend_event
    
    caller_type = int(caller_type)
    person = get_or_create_person(person_id)
    
    if caller_type == ACTION_TYPES['EVENT']:
        PersonEvent.objects.create(person=person, event_name=caller_name, event_value=caller_value)
    elif caller_type == ACTION_TYPES['CONTACT']:
        try:
            PersonContact.objects.create(person=person, contact_type=caller_name, contact_value=caller_value)
        except IntegrityError:
            pass
    elif caller_type == ACTION_TYPES['DATA']:
        try:
            PersonData.objects.create(person=person, data_type=caller_name, data_value=caller_value)
        except IntegrityError:
            pass
    else:
        print("some error")

    return handle_backend_event(caller_type, person_id, caller_name, caller_value)
