import uuid
from .models import Person, PersonVisit, PersonContact, PersonEvent, PersonData


def create_new_site_visitor() -> Person:
    person = Person()
    person.save()
    return person


def track_person_visit(person_id: str, page: str, user_agent: str, user_ip: str) -> Person:
    person_object = _get_or_create_person(person_id)
    user_agent = user_agent if user_agent is not None else ''
    user_ip = user_ip if user_ip is not None else ''
    PersonVisit.objects.create(person=person_object, page=page, user_agent=user_agent, user_ip=user_ip)
    return person_object


def attach_contact_to_person(person_id: str, contact_type: str, contact_value: str) -> Person:
    person_object = _get_or_create_person(person_id)
    # TODO: catch exceptions
    person_info = PersonContact.objects.create(person=person_object, contact_type=contact_type, contact_value=contact_value)
    return person_info.person


def attach_data_to_person(person_id: str, data_type: str, data_value: str) -> Person:
    person_object = _get_or_create_person(person_id)
    # TODO: catch exceptions
    person_data = PersonData.objects.create(person=person_object, data_type=data_type, data_value=data_value)
    return person_data.person


def send_person_event(person_id: str, event_name: str, event_value: str) -> Person:
    person_object = _get_or_create_person(person_id)
    person_event = PersonEvent.objects.create(person=person_object, event_name=event_name, event_value=event_value)
    return person_event.person


def _get_or_create_person(uid) -> Person:
    person_id = _uid_or_none(uid)
    person_object = Person.objects.filter(uid=person_id).first()
    if person_object is None:
        person_object = create_new_site_visitor()
    return person_object


def _uid_or_none(uid) -> str:
    return uid if _validate_uuid(uid) else None


def _validate_uuid(uid) -> bool:
    try:
        uuid.UUID(uid, version=1)
        return True
    except Exception:
        return False
