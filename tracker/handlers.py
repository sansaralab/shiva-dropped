from django.core.exceptions import ObjectDoesNotExist
from .models import Trigger, Person
from .types import TRIGGER_REACTION_SIDES, HandlerResponse
from .services import get_or_create_person
from .tasks import handle_background


def handle(action_type, person_id, param_name, param_value):
    person_object = get_or_create_person(person_id)

    javascripts = handle_frontend_event(action_type, person_object, param_name, param_value)
    send_to_queue(action_type, str(person_object.uid), param_name, param_value)
    response = HandlerResponse(person=person_object, javascript=javascripts)

    return response


def handle_frontend_event(action_type, person: Person, event_name: str, event_value: str):
    javascripts = list()

    try:
        triggers = Trigger.objects.filter(reaction_side=TRIGGER_REACTION_SIDES['FRONTEND']).get()
    except ObjectDoesNotExist:
        triggers = list()

    if len(triggers):
        for trigger in triggers:
            pass

    return javascripts


def handle_backend_event(action_type, person_id, action_name, action_value):
    try:
        triggers = Trigger.objects.filter(reaction_side=TRIGGER_REACTION_SIDES['BACKEND']).get()
    except ObjectDoesNotExist:
        triggers = list()

    if len(triggers):
        for trigger in triggers:
            pass

    return True


def send_to_queue(action_type, person_id, action_name, action_value):
    # FIXME: when .delay - celery not work
    handle_background(caller_type=action_type, person_id=person_id, caller_name=action_name, caller_value=action_value)
