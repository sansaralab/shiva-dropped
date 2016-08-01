import time
from .models import Trigger, Person
from .types import TRIGGER_ACTION_TYPES, HandlerResponse
from .services import get_or_create_person
from .tasks import handle_background


def handle(caller_type, person_id, caller_name, caller_value):
    person_object = get_or_create_person(person_id)

    javascripts = handle_frontend_event(person_object, caller_name, caller_value)
    send_to_queue(caller_type, str(person_object.uid), caller_name, caller_value)
    response = HandlerResponse(person=person_object, javascript=javascripts)

    return response


def handle_frontend_event(person: Person, event_name: str, event_value: str):
    javascripts = list()
    triggers = Trigger.objects.filter(action_type=TRIGGER_ACTION_TYPES['FRONTEND']).all()

    if len(triggers):
        for trigger in triggers:
            pass

    return javascripts


def send_to_queue(caller_type, person_id, caller_name, caller_value):
    # FIXME: when .delay - celery not work
    handle_background.delay(caller_type=caller_type, person_id=person_id, caller_name=caller_name, caller_value=caller_value)
