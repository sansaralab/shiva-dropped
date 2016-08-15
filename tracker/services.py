import uuid
from .types import ACTION_TYPES
from .models import Person, PersonVisit, PersonContact, PersonEvent, PersonData, Trigger


def create_new_site_visitor(uid='') -> Person:
    if _validate_uuid(uid):
        person = Person.objects.create(uid=uid)
    else:
        person = Person.objects.create()
    return person


def track_person_visit(person_id: str, page: str, user_agent: str, user_ip: str) -> Person:
    person_object = get_or_create_person(person_id)
    user_agent = user_agent if user_agent is not None else ''
    user_ip = user_ip or ''
    PersonVisit.objects.create(person=person_object, page=page, user_agent=user_agent, user_ip=user_ip)
    return person_object


def attach_contact_to_person(person_id: str, contact_type: str, contact_value: str) -> Person:
    from .handlers import handle
    response = handle(ACTION_TYPES['CONTACT'], person_id, contact_type, contact_value)
    return response


def attach_data_to_person(person_id: str, data_type: str, data_value: str) -> Person:
    from .handlers import handle
    response = handle(ACTION_TYPES['DATA'], person_id, data_type, data_value)
    return response


def send_person_event(person_id: str, event_name: str, event_value: str) -> Person:
    from .handlers import handle
    response = handle(ACTION_TYPES['EVENT'], person_id, event_name, event_value)
    return response


def get_triggers_conditions():
    conditions = Trigger.objects.values_list('conditions', flat=True)
    return conditions


def get_or_create_person(uid) -> Person:
    person_id = _uid_or_none(uid)
    person_object = Person.objects.filter(uid=person_id).first()
    return person_object or create_new_site_visitor(uid)


def _uid_or_none(uid) -> str:
    return uid if _validate_uuid(uid) else None


def _validate_uuid(uid) -> bool:
    try:
        uuid.UUID(uid, version=1)
        return True
    except Exception:
        return False
