import uuid
from .models import Person, PersonVisit, PersonInfo, PersonEvent


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


def attach_info_to_person(person_id: str, info_type: str, info_value: str) -> Person:
    person_object = _get_or_create_person(person_id)
    person_info = PersonInfo.objects.create(person=person_object, info_type=info_type, info_value=info_value)
    return person_info.person


def send_person_event(person_id: str, event_name: str, event_value: str) -> Person:
    person_object = _get_or_create_person(person_id)
    person_event = PersonEvent.objects.create(person=person_object, event_name=event_name, event_value=event_value)
    return person_event.person


def _get_or_create_person(uid):
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
