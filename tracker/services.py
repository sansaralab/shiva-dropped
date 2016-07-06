import uuid
from .models import Person, PersonVisit


def create_new_site_visitor() -> Person:
    person = Person()
    person.save()
    return person


def track_person_visit(person_id: str, page: str, user_agent: str, user_ip: str) -> str:
    try:
        uuid.UUID(person_id, version=1)
    except Exception:
        person_id = None
    person_object = Person.objects.filter(uid=person_id).first()
    if person_object is None:
        person_object = create_new_site_visitor()
    user_agent = user_agent if user_agent is not None else ''
    user_ip = user_ip if user_ip is not None else ''
    visit = PersonVisit(person=person_object, page=page, user_agent=user_agent, user_ip=user_ip)
    visit.save()
    return person_object.uid
